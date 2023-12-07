import os
import sqlalchemy
from google.cloud.sql.connector import Connector


# def conn_str() -> str:
#     PASSWORD = "root"
#     PUBLIC_IP_ADDRESS = "35.194.194.150"
#     DBNAME = "newsdb"
#     PROJECT_ID = "cloud-sql-407317"
#     INSTANCE_NAME = "cloudmysql"
#     return f"mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}?charset=utf8mb4"


def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a Unix socket connection pool for a Cloud SQL instance of MySQL."""
    db_user = os.environ["DB_USER"]  # e.g. 'my-database-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-database-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    unix_socket_path = os.environ["INSTANCE_UNIX_SOCKET"]  # e.g. '/cloudsql/project:region:instance'
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={"unix_socket": unix_socket_path},
        ),
    )
    return pool


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
