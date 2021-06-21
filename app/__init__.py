import os
from datetime import datetime
from enum import unique
from logging import debug
from os import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5f47fc632a585184688be1969d20bfcb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in'


app.config['MAIL_SERVER'] = 'smtp.google.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "taskboardteam@gmail.com"
app.config['MAIL_PASSWORD'] = "taskboard1234"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)




from app import routes