import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    if request.method == "GET":
        userID = session["user_id"]
        userInfo = db.execute("SELECT username, cash FROM users WHERE id = ?", userID)
        username = userInfo[0]['username']
        cash = round(userInfo[0]['cash'],2)
        transactions = db.execute("SELECT symbol, SUM(qty) as totalQty FROM transactions WHERE username = ? GROUP BY symbol HAVING totalQty > 0", username)
        accountValue = cash
        for transaction in transactions:
            symbol = transaction['symbol']
            shares = transaction['totalQty']
            quote = lookup(symbol)
            price = quote['price']
            transaction['price'] = price
            total = float(price) * float(shares)
            transaction['total'] = round(total,2)
            accountValue += total
        accountValue = round(accountValue,2)
        return render_template("index.html", transactions=transactions, cash=cash, accountValue=accountValue)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must enter deposit amount!", 400)
        quotedSymbol = lookup(symbol)
        if quotedSymbol is None:
            return apology("Symbol not found!", 400)
        shares = request.form.get("shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("must be number!", 400)
        if shares < 1:
            return apology("must enter > 1!", 400)

        userID = session["user_id"]
        if userID == None:
            return redirect("/login")
        symbolCost = quotedSymbol['price']
        totalPurchase = symbolCost * shares
        userInfo = db.execute("SELECT * FROM users WHERE id = ?", userID)
        cash = userInfo[0]['cash']
        username = userInfo[0]['username']
        buy = 'buy'
        if totalPurchase > cash:
            return apology("insufficient Funds!", 400)
        db.execute("INSERT INTO transactions (username, symbol, qty, total, type) VALUES(?, ?, ?, ?, ?)", username, quotedSymbol['symbol'], shares, totalPurchase, buy)
        updatedUserCash = cash - totalPurchase
        db.execute("UPDATE users SET cash = ? WHERE id = ?", updatedUserCash, userID)
    return redirect("/")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        userID = session["user_id"]
        userInfo = db.execute("SELECT username, cash FROM users WHERE id = ?", userID)
        username = userInfo[0]['username']
        transactions = db.execute("SELECT * FROM transactions WHERE username = ?", username)
        return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Symbol Required!", 400)
        quotedSymbol = lookup(symbol)
        if quotedSymbol is None:
            return apology("Symbol not found!", 400)
        return render_template("quoted.html", quotedSymbol=quotedSymbol)

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("Username error!", 400)
        if len(username) < 3 or len(username) > 12:
            return apology("3-12 char required!", 400)
        if db.execute("SELECT username FROM users WHERE username = ?", username) != []:
            return apology("Username in use!", 400)
        password = request.form.get("password")
        if not password:
            return apology("Password required!", 400)
        if len(password) < 8 or len(password) > 16:
            return apology("8-16 length required", 400)
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("Password confirmation missing!", 400)
        if len(confirmation) < 8 or len(confirmation) > 16:
            return apology("8-16 length required", 400)
        if password != confirmation:
            return apology("passwords must match", 400)
        hashedPassword = generate_password_hash(password)
        starterCash = 10000
        db.execute("INSERT INTO users (username, hash, cash) VALUES(?, ?, ?)", username, hashedPassword, starterCash)
        return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    userID = session["user_id"]
    userInfo = db.execute("SELECT username, cash FROM users WHERE id = ?", userID)
    username = userInfo[0]['username']
    cash = userInfo[0]['cash']
    if request.method == "GET":
        stocks = db.execute("SELECT symbol FROM transactions WHERE username = ? GROUP BY symbol", username)
        for stock in stocks:
            symbol = stock['symbol']
        return render_template("sell.html", stocks=stocks)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
             return apology("missing symbol", 400)
        s = int(request.form.get("shares"))
        if s <= 0:
            return apology("Invalid share qty", 400)
        shares = -s
        if not shares:
             return apology("Missing share qty", 400)
        holdings = db.execute("SELECT symbol, sum(qty) as totalQty FROM transactions WHERE username = ? and symbol = ? GROUP BY symbol", username, symbol)
        # This will return symbol (eg NFLX) and totalQty (eg 6)
        if holdings == []:
            return apology("symbol not owned", 400)
        if holdings[0]['totalQty'] < s:
            return apology("excessive sale qty", 400)
        quote = lookup(symbol)
        price = quote['price']
        saleValue = round(price * s, 2)
        cash += saleValue
        # Add sale value to user account
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, userID)
        # Add to transactions
        sell = 'sell'
        db.execute("INSERT INTO transactions (username, symbol, qty, total, type) VALUES(?, ?, ?, ?, ?)", username, symbol, shares, saleValue, sell)
        return redirect("/")


# account functionality

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Change password"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("password") or not request.form.get("newPassword") or not request.form.get("confirmPassword"):
            return apology("fields cannot be blank!", 403)
        userID = session["user_id"]
        userInfo = db.execute("SELECT * FROM users WHERE id = ?", userID)
        if not check_password_hash(userInfo[0]["hash"], request.form.get("password")):
            return apology("invalid password", 403)

        newPassword = request.form.get("newPassword")
        if not newPassword:
            return apology("Password missing", 403)
        if len(newPassword) < 8 or len(newPassword) > 16:
            return apology("8-16 length required", 403)
        confirmPassword = request.form.get("confirmPassword")
        if not confirmPassword:
            return apology("Password confirmation missing", 403)
        if len(confirmPassword) < 8 or len(confirmPassword) > 16:
            return apology("8-16 length required", 403)
        if newPassword != confirmPassword:
            return apology("Password must match", 403)
        hashedPassword = generate_password_hash(newPassword)
        db.execute("UPDATE users SET hash = ? WHERE ID = ?", hashedPassword, userID)
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("account.html")

@app.route("/deposit", methods=["POST"])
@login_required
def deposit():
    """Deposit funds to account"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("deposit"):
            return apology("must enter deposit amount!", 403)
        deposit = int(request.form.get("deposit"))
        if deposit < 1 or deposit > 1000000:
            return apology("deposit between $1 and $1000000")
        userID = session["user_id"]
        userInfo = db.execute("SELECT username, cash FROM users WHERE id = ?", userID)
        cash = userInfo[0]['cash']
        username = userInfo[0]['username']
        newValue = cash + deposit
        symbol = 'n/a'
        qty = '0'
        type = 'deposit'
        db.execute("UPDATE users SET cash = ? WHERE ID = ?", newValue, userID)
        db.execute("INSERT INTO transactions (username, symbol, qty, total, type) VALUES(?, ?, ?, ?, ?)", username, symbol, qty, deposit, type)
        return redirect("/")

