from datetime import datetime
from enum import unique
from logging import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5f47fc632a585184688be1969d20bfcb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in'


from app import routes