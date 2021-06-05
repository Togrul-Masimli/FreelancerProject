from datetime import datetime
from enum import unique
from logging import debug
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '5f47fc632a585184688be1969d20bfcb'

from app import routes