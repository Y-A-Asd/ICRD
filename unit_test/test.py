from core.database.database_engines import engine,DatabaseConnectionManager
from core.database.classes_structure import Base
from core.database.classes import Department,Payslip, MODEL
from temp_data.read_json import manage_data
from core.crudORM.selection import selection
from core.crudORM.insertion import Insertion
from core.crudORM.updation import Updation
from core.crudORM.deletion import Deletion
import pytest



class Test_SQLALchemy:
    Base.metadata.create_all(engine)
    conn = engine.connect()

    def test_selection(self):
        select = selection(self.conn)
        res = select.select("department", id=3)
        assert dict(res)["id"] ==3 and dict(res)["name"] =="Dabfeed"
    def test_insertion(self):
        insertion = Insertion(self.conn)
        column_data = {"id":99999999,"name":"temp_test","phone":00000000}
        insertion.insert_data(table_name="department",column_data=column_data)
        select = selection(self.conn)
        res = select.select("department", id=99999999)
        assert dict(res)["id"] == 99999999 and dict(res)["name"] == "temp_test"

    def test_deletion(self):
        dele = Deletion(self.conn)
        dele.delete("department", id=99999999)


    # def test_updation(self):
    #     up = Updation(self.conn)
    #     up.update("department", id=5)



class Test_Model:
    db = DatabaseConnectionManager()
    MODEL.conn = db

    def test_get_v1(self):
        d = Department.get(name="Dabfeed", id=3)
        assert d.name == "Dabfeed"

    def test_get_v2(self):
        p = Payslip.get(id=9)
        assert float(p.base) == 1076.37

    def test_fromid_v1(self):
        d = Department.from_id(3)
        assert d.name == "Dabfeed" and d.phone == "8851904171"

    def test_save(self):
        d = Department(99999999, "test_temp", "000000000")
        d.save()
        d = Department.get(id=99999999)
        assert d.name=="test_temp"

    def test_update(self):
        d = Department.get(id=99999999)
        d.phone = 123456789
        d.update()
        d1 = Department.get(id=99999999)
        assert int(d1.phone) == 123456789

    def test_delete(self):
        d = Department.get(id=99999999)
        d.delete()
        d = Department.get(id = 99999999)
        assert d == "Multiple objects found for Department with kwargs {'id': 99999999}"
    def test(self):
        pytest.main(["-v"], plugins=[Test_Model()])
