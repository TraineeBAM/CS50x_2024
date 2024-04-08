from flask import Flask

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = './app/'

from app import routes