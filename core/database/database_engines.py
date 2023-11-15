import dotenv
import sqlalchemy
import os
import platform
import subprocess
import sys
import psycopg2
from psycopg2.errors import OperationalError,UniqueViolation
from sqlalchemy import Engine

dotenv.load_dotenv()

host = os.getenv("host")
database = os.getenv("database")
password = os.getenv("password")
user = os.getenv("user")


# engine = create_engine(dialect+driver://username:password@host:port/database_name)
engine: Engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:5432/{database}")


class DatabaseConnectionManager:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database=database, user=user,password=password, host=host)
        except OperationalError:
            exit("POSTGRESQL SERVICE NOT RUNNING!")

    def close(self):
        self.conn.close()

    def execute(self, query, params=[]):
        try:
            with self.conn as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)
                conn.commit()
                return cursor
        except UniqueViolation:
            pass


    def execute_without_commit(self,query,params=[]):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor




def start_postgresql():
    if platform.system() == "Linux":
        subprocess.run("systemctl start postgresql", shell=True)
    elif platform.system() == "Windows":
        service_name = "PostgreSQL"  #???
        subprocess.run(f"net start {service_name}", shell=True)

def is_postgresql_running():
    if platform.system() == "Linux":
        result = subprocess.run("systemctl is-active postgresql", shell=True, capture_output=True)
        return result.returncode == 0
    elif platform.system() == "Windows":
        service_name = "PostgreSQL"
        result = subprocess.run(f"sc query {service_name}", shell=True, capture_output=True)
        return "RUNNING" in result.stdout.decode()
