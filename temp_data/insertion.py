from core.database.engine import engine
from sqlalchemy import insert, Table
from sqlalchemy.orm import Session
from core.classes.classes_structure import Base,Department,Employee,Payment,Payslip,Project,Employeeprojectrelation,Attendance,Salary
from sqlalchemy.exc import IntegrityError,NoSuchTableError,InternalError

def exeption_dec(func):
    def wrapper(self, *args, **kwargs):
        session = Session(bind=self.conn)
        try:
            func(self, *args, **kwargs)
            session.commit()
        except (InternalError,IntegrityError) as e:
            print(f"Duplicate data or integrity constraint violation.\n{e}")
            session.rollback()  # Roll back the transaction in case of an error
        finally:
            session.close()
    return wrapper

class Insertion:
    def __init__(self,conn):
        self.conn = conn
    @exeption_dec
    def insert_data(self, table_name:str, column_data):
        table = Table(table_name.capitalize(), Base.metadata, autoload_with=self.conn)
        insertion = insert(table).values(**column_data)
        # print(column_data)
        self.conn.execute(insertion)



