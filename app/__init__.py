from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .analysis import Analysis


def conn_str() -> str:
    PASSWORD = "root"
    PUBLIC_IP_ADDRESS = "35.194.194.150"
    DBNAME = "newsdb"
    PROJECT_ID = "cloud-sql-407317"
    INSTANCE_NAME = "cloudmysql"
    return f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}?charset=utf8mb4"


app = Flask(__name__)
app.secret_key = '1234567890qwertyuiop'
app.config['PAGE_SIZE'] = 10
app.config["SQLALCHEMY_DATABASE_URI"] = conn_str()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
