import dotenv
import sqlalchemy
import os
import psycopg2
from sqlalchemy import Engine

dotenv.load_dotenv()

host = os.getenv("host")
database = os.getenv("database")
password = os.getenv("password")
user = os.getenv("user")


# engine = create_engine(dialect+driver://username:password@host:port/database_name)
engine: Engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{user}@{host}:5432/{database}")


class DatabaseConnectionManager:
    def __init__(self):
        self.conn = psycopg2.connect(database=database, user=user, host=host)

    def close(self):
        self.conn.close()

    def execute(self, query, params=[]):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def execute_without_commit(self,query,params=[]):
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor