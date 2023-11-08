import dotenv
import sqlalchemy
import os

dotenv.load_dotenv()

host = os.getenv("host")
database = os.getenv("database")
password = os.getenv("password")
user = os.getenv("user")
# engine = create_engine(dialect+driver://username:password@host:port/database_name)
engine = sqlalchemy.create_engine(f"postgresql+psycopg2://{user}@{host}:5432/{database}")

