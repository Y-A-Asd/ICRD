from typing import Any, List,Optional
from core.database.engine import engine
import dotenv
import psycopg2
import os
dotenv.load_dotenv()
host = os.getenv("host")
database = os.getenv("database")
password = os.getenv("password")
user = os.getenv("user")

class DatabaseConnectionManager:

    def __init__(self, engin: engine):
        self.connection = psycopg2.connect(database=database,user=user,host=host)

    def close(self):
        self.connection.close()

    def execute(self, query, params=[]):
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor


class MODEL:
    __conn = None

    def __init__(self, conn: DatabaseConnectionManager) -> None:
        self.conn = conn

    @classmethod
    def from_id(cls, id: int) -> Optional:
        query = f"SELECT * FROM {cls.__name__} WHERE id = ?"
        params = [id]
        results = cls.conn.execute(query, params)
        if len(results) == 1:
            return cls(cls.conn, **results[0])
        else:
            return None

    @classmethod
    def get(cls, **kwargs) -> Any:
        query = f'SELECT * FROM "{cls.__name__}" WHERE {"AND ".join([f"{key} = %s" for key in kwargs.keys()])};'
        params = list(kwargs.values())
        result = cls.conn.execute(query, params)
        data = result.fetchall()
        try :
            return cls(*data[0])
        except IndexError:
            return f"Multiple objects found for {cls.__name__} with kwargs {kwargs}"


    @classmethod
    def filter(cls, **kwargs):
        cursor = cls.conn.cursor()
        query = f"SELECT * FROM {cls.__class__.__name__} WHERE {', '.join([f'{key}=?' for key in kwargs.keys()])}"
        params = list(kwargs.values())

        cursor.execute(query, params)
        rows = cursor.fetchall()

        return [cls(cls.conn, **{key: value for key, value in zip(cls.__dict__.keys(), row)}) for row in rows]

    def save(self) -> None:
        query = f"INSERT INTO {self.__class__.__name__} ({', '.join(self.__dict__.keys())}) VALUES ({', '.join(['?' for key in self.__dict__.keys()])})"
        params = list(self.__dict__.values())
        self.conn.execute(query, params)

    def update(self) -> None:
        query = f"UPDATE {self.__class__.__name__} SET {', '.join([f'{key}=?' for key in self.__dict__.keys()])} WHERE id = ?"
        params = list(self.__dict__.values()) + [self.id]
        self.conn.execute(query, params)

    def delete(self) -> None:
        query = f"DELETE FROM {self.__class__.__name__} WHERE id = ?"
        params = [self.id]
        self.conn.execute(query, params)


class Department(MODEL):
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name}, phone={self.phone})"


class Employee:
    def __init__(self, conn, id, account, department, phone):
        super().__init__(conn)
        self.id = id
        self.account = account
        self.department = department
        self.phone = phone

    def __repr__(self):
        return f"Employee(id={self.id}, account={self.account}, department={self.department}, phone={self.phone})"


class Project:
    def __init__(self, connection, id, title, department, estimated_end_time, end_time):
        self.id = id
        self.title = title
        self.department = department
        self.estimated_end_time = estimated_end_time
        self.end_time = end_time

    def __repr__(self):
        return f"Project(id={self.id}, title={self.title}, department={self.department}, estimated_end_time={self.estimated_end_time}, end_time={self.end_time})"


class Employeeprojectrelation:
    def __init__(self, connection, id, employee, project, hours, role):
        super().__init__(connection)
        self.id = id
        self.employee = employee
        self.project = project
        self.hours = hours
        self.role = role

    def __repr__(self):
        return f"Employeeprojectrelation(id={self.id}, employee={self.employee}, project={self.project}, hours={self.hours}, role={self.role})"


class Attendance:
    def __init__(self, connection, id, employee, date, in_time, out_time, late_cause):
        super().__init__(connection)
        self.id = id
        self.employee = employee
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.late_cause = late_cause

    def __repr__(self):
        return f"Attendance(id={self.id}, employee={self.employee}, date={self.date}, in_time={self.in_time}, out_time={self.out_time}, late_cause={self.late_cause})"


class Salary:
    def __init__(self, connection, id, employee, base, tax, insurance, overtime):
        super().__init__(connection)
        self.id = id
        self.employee = employee
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime

    def __repr__(self):
        return f"Salary(id={self.id}, employee={self.employee}, base={self.base}, tax={self.tax}, insurance={self.insurance}, overtime={self.overtime})"


class Payment:
    def __init__(self, connection, amount, account_number, payment_type, description, date):
        self.amount = amount
        self.account_number = account_number
        self.payment_type = payment_type
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Payment(id={self.id}, amount={self.amount}, account_number={self.account_number}, payment_type={self.payment_type}, description={self.description}, date={self.date})"


class Payslip:

    def __init__(self, id, base, tax, insurance, overtime, salary, created, payment):
        self.id = id
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime
        self.salary = salary
        self.created = created
        self.payment = payment

    def __repr__(self):
        return f"Payslip(id={self.id}, base={self.base}, tax={self.tax}, insurance={self.insurance}, overtime={self.overtime}, salary={self.salary}, created={self.created}, payment={self.payment})"
