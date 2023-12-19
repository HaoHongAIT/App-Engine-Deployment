from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .analysis import Analysis
from .database import get_conn
from flask_login import LoginManager
import app.database as database

app = Flask(__name__)
app.secret_key = '1234567890qwertyuiop'
app.config['PAGE_SIZE'] = 10
# app.config["SQLALCHEMY_DATABASE_URI"] = database.conn_str()
# configure Flask-SQLAlchemy to use Python Connector
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"creator": database.get_conn}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
login_manager = LoginManager(app=app)
