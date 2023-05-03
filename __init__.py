from flask import Flask, render_template
from .models import db
import secrets
import os

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Kuliah/Semester 8/#SKRIPSI/#DEV/Web/Cowding/Database/DBskripsi.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/DBskripsi.db')
db.init_app(app)

secret_key = secrets.token_hex(16)
app.secret_key = secret_key


#Register Blueprints
from .auth import auth
app.register_blueprint(auth)

from .stockdata import stockdata
app.register_blueprint(stockdata)

from .Nav import Nav
app.register_blueprint(Nav)
