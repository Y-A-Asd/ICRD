from core.database.engine import engine
from core.classes.classes_structure import Base
import time
print("WE ARE WORKING PLEASE WAIT ",end=" ")
time.sleep(1)
print("...",end="")
time.sleep(1)
print("...",end="")
time.sleep(1)
print("...",end="")
time.sleep(2)

from temp_data.read_json import manage_data
Base.metadata.create_all(engine)
with engine.connect() as conn:
    manage_data(conn)

