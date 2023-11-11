from core.database.database_engines import engine,DatabaseConnectionManager
from core.database.classes_structure import Base
from core.database.classes import Attendance,Department,MODEL
from core.crudORM.selection import selection
from core.crudORM.updation import Updation
from core.crudORM.deletion import Deletion
from unit_test.test import Test_Model
from core.query.query_gen import run_all_query
import time
from temp_data.read_json import manage_data
import os
import subprocess
import pytest


def fundamental():
    print("RUNING POSTGRESQL SERVICE!")
    subprocess.run("systemctl start postgresql",shell= True)
    time.sleep(1)
    print("INITIALISING DATABASE ENGINE!")
    time.sleep(1)
    print("MAKING TABLES READY!")
    Base.metadata.create_all(engine)
    time.sleep(1)
    print("RUNING SELF TEST...",end="")
    pytest.main(["-q","unit_test/test.py::Test_Model"])
    time.sleep(1)
    print("RUNING QUERIES")
    run_all_query()

#300,116,2000,09:00:00














fundamental()
# with engine.connect() as conn:
    # temp dat
    # manage_data(conn)

    #selection
    # select = selection(conn)
    # res = select.select("department", id=3)
    # print (dict(res))


    #updation
    # up = Updation(conn)
    # up.update("department", id=5)

    #deletion
    # delp = Deletion(conn)
    # delp.delete("department", id=5)

# db=DatabaseConnectionManager(engine)
# model = MODEL(db)
# Department.conn = db
# d= Department.get(name="Dabfeed",id=4)
# print(type(Department.get(name="Dabfeed",id=3)))



# db = DatabaseConnectionManager(engine)
# MODEL.conn = db
# d = Department.get(id=99999999)
# d.phone=111111111
# d.update()
# print(d)




