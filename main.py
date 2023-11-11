from core.database.database_engines import engine,DatabaseConnectionManager
from core.database.classes_structure import Base
from temp_data.json_to_db import json_to_db_self_orm
from core.query.query_gen import run_all_query
import time
from core.crudORM.selection import selection
from temp_data.read_json import manage_data
import os
import subprocess
import pytest


def fundamental():
    print("RUNING POSTGRESQL SERVICE!")
    subprocess.run("systemctl start postgresql",shell= True)
    time.sleep(0.5)
    print("INITIALISING DATABASE ENGINE!")
    time.sleep(0.5)
    print("MAKING TABLES READY!")
    Base.metadata.create_all(engine)
    time.sleep(0.5)
    print("READING DATA FROM JSON!")
    json_to_db_self_orm()
    time.sleep(0.5)
    print("RUNING SELF TEST...",end="")
    pytest.main(["-q","unit_test/test.py"])
    time.sleep(0.5)
    print("RUNING QUERIES")
    run_all_query()

#300,116,2000,09:00:00




if __name__ == "__main__":
    fundamental()










# d = Department(**{"id":9,"name":"dd","phone":900276235})
# print(d)
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




