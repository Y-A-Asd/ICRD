from core.database.engine import engine
from core.database.classes_structure import Base
from core.database.classes import Department,MODEL,DatabaseConnectionManager
from core.crudORM.selection import selection
from core.crudORM.updation import Updation
from core.crudORM.deletion import Deletion
import time
from temp_data.read_json import manage_data


# print("WE ARE WORKING PLEASE WAIT ",end=" ")
# time.sleep(1)
# print("...",end="")
# time.sleep(1)
# print("...",end="")
# time.sleep(1)
# print("...",end="")
# time.sleep(2)

Base.metadata.create_all(engine)
# with engine.connect() as conn:
    # temp dat
    # manage_data(conn)

    #selection
    # select = selection(conn)
    # select.select("department", id=3)


    #updation
    # up = Updation(conn)
    # up.update("department", id=5)

    #deletion
    # delp = Deletion(conn)
    # delp.delete("department", id=5)

db=DatabaseConnectionManager(engine)
model = MODEL(db)
Department.conn = db
d= Department.get(name="Dabfeed",id=4)
print(d)




