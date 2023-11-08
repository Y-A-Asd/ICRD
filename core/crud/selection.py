from sqlalchemy import select,Table,and_
from core.database.classes_structure import Base


class selection:
    def __init__(self, conn):
        self.conn = conn

    def select(self, table_name,**kwargs):
        table = Table(table_name.capitalize(), Base.metadata, autoload_with=self.conn)
        selection = select(table).filter_by(**kwargs)
        result = self.conn.execute(selection)
        column_names = [column.name for column in table.columns]
        result = result.fetchall()
        if result == []:
            print("No data found!")
        for data in result:
            out = list(zip(column_names,data))
            print("    ".join(f"{key},{value}" for key,value in out).replace(","," : "))



