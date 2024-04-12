from flask import Flask
import os

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = './app/'
app.secret_key = os.urandom(24)

from app import routes