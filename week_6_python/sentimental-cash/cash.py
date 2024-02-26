import cs50

answer = 0
while True:
    try:
        change = cs50.get_float("Change: ")
        if change >= 0.01:
            break
    except ValueError:
        print("Please enter a value greater than 0.1")

change = change * 100
quarter = change // 25
answer += quarter
change -= quarter * 25
dime = change // 10
answer += dime
change -= dime * 10
nickel = change // 5
answer += nickel
change -= nickel * 5
penny = change // 1
answer += penny

print(int(answer))
