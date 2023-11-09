from sqlalchemy import delete,Table,and_
from core.database.classes_structure import Base


class Deletion:
    def __init__(self, conn):
        self.conn = conn

    def delete(self, table_name,**kwargs):
        table = Table(table_name.capitalize(), Base.metadata, autoload_with=self.conn)
        where_clause = and_(*[getattr(table.c, key) == value for key, value in kwargs.items()])

        deletion = delete(table).where(where_clause)
        self.conn.execute(deletion)
        status = input("R u sure? (y/n): ")
        if status.lower() == "y":
            self.conn.commit()
        else:
            self.conn.rolleback


