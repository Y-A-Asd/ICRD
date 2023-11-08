from sqlalchemy import select,Table,update,and_
from core.database.classes_structure import Base


class Updation:
    def __init__(self, conn):
        self.conn = conn

    def update(self, table_name, **kwargs):
        table = Table(table_name.capitalize(), Base.metadata, autoload_with=self.conn)
        column_names = [column.name for column in table.columns]
        print("Available columns:", column_names)

        print("Which column/s do you want to update?")
        columns_to_update = input("Enter column names separated by commas: ").split(',')
        values_to_update = {}

        for column in columns_to_update:
            if column.strip() in column_names:
                values_to_update[column.strip()] = input(f"Enter new value for {column.strip()}: ")

        self.do_update(table, kwargs, values_to_update)

    def do_update(self, table, filter_conditions, update_values):
        if len(update_values) > 0:
            where_clause = and_(*[getattr(table.c, key) == value for key, value in filter_conditions.items()])
            # print(where_clause)
            updation = update(table).where(where_clause).values(update_values)
            self.conn.execute(updation)
            self.conn.commit()
            print("Record updated successfully!")
        else:
            print("No values input!")

