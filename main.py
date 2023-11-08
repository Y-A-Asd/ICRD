from core.database.engine import engine
from core.database.classes_structure import Base
from core.crud.selection import selection
from core.crud.updation import Updation
from core.crud.deletion import Deletion
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
with engine.connect() as conn:
    # temp data
    manage_data(conn)

    #selection
    # select = selection(conn)
    # select.select("department", id=3)


    #updation
    # up = Updation(conn)
    # up.update("department", id=5)

    #deletion
    # delp = Deletion(conn)
    # delp.delete("department", id=5)



