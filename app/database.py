import os
import sqlalchemy
from google.cloud.sql.connector import Connector


def conn_str() -> str:
    PASSWORD = "root"
    PUBLIC_IP_ADDRESS = "35.201.199.171"
    DBNAME = "newsdb"
    PROJECT_ID = "delpoy-webapp"
    INSTANCE_NAME = "cloudsql"
    return f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}?charset=utf8mb4"


def get_conn():
    db_user = os.environ.get('CLOUD_SQL_USERNAME')
    db_pass = os.environ.get('CLOUD_SQL_PASSWORD')
    db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
    db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
    with Connector() as connector:
        conn = connector.connect(
            db_connection_name,
            "pymysql",
            user=db_user,
            password=db_pass,
            db=db_name)
    return conn
