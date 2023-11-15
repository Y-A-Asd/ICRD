from temp_data.read_json import manage_data
from core.crudORM.insertion import Insertion
from core.database.database_engines import engine
from core.database.classes import MODEL,Attendance,Department,Payment,Project,Payslip,Employee,Employeeprojectrelation,Salary
from core.database.database_engines import DatabaseConnectionManager
import sys
from psycopg2.errors import UniqueViolation,InFailedSqlTransaction
manage_data()


def json_to_db_alchemy():
    with engine.connect() as conn:
        insertion = Insertion(conn)
        count_data = 0
        for table,column_data in manage_data():
            try:
                insertion.insert_data(table_name=table,column_data=column_data)
            except Exception:
                pass
            finally:
                count_data += 1
    print(count_data, "DATA WERE ADDED!")
def json_to_db_self_orm():
    db = DatabaseConnectionManager()
    MODEL.conn = db
    count_data = 0
    for table,column_data in manage_data():
        table = getattr(sys.modules[__name__], table.capitalize()) #LIL MAGIC :)
        temp_obj: MODEL = table(**column_data)
        temp_obj.save()
        count_data += 1
    print(count_data,"DATA WERE ADDED!")





