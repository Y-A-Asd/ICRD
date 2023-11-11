from typing import Any, List, Optional


class MODEL:
    """
    MAGIC IS HERE !
    """
    __conn = None

    @classmethod
    def get(cls, **kwargs) -> Any:
        table = cls.__name__
        query = f'SELECT * FROM "{table}" WHERE {"AND ".join([f"{key} = %s" for key in kwargs.keys()])};'
        params = list(kwargs.values())
        result = cls.conn.execute_without_commit(query, params)
        data = result.fetchall()
        try:
            return cls(*data[0])  # MAGIC :)
        except IndexError:
            return f"Multiple objects found for {table} with kwargs {kwargs}"

    @classmethod
    def from_id(cls, id: int) -> List:
        table = cls.__name__
        query = f'SELECT * FROM "{table}" WHERE id = %s'
        params = [id]
        results = cls.conn.execute_without_commit(query, params)
        data = results.fetchall()
        try:
            return cls(*data[0])  # MAGIC :)
        except IndexError:
            return f"objects not found for {table} "

    @classmethod
    def filter(cls, **kwargs):
        query = f'SELECT * FROM "{cls.__name__}" WHERE {"AND ".join([f"{key}= %s" for key in kwargs.keys()])}'
        params = list(kwargs.values())
        results = cls.conn.execute_without_commit(query, params)
        data = results.fetchall()
        obj_list = []
        for obj in data:
            obj_list.append(cls(*obj))
        return obj_list

    def save(self) -> None:
        query = f'INSERT INTO "{self.__class__.__name__}" ({", ".join(self.__dict__.keys())}) VALUES ({", ".join(["%s" for key in self.__dict__.keys()])})'
        params = list(self.__dict__.values())
        self.conn.execute(query, params)

    def update(self) -> None:
        query = f'UPDATE "{self.__class__.__name__}" SET {", ".join([f"{key}=%s" for key in self.__dict__.keys()])} WHERE id = %s'
        params = list(self.__dict__.values()) + [self.id]
        self.conn.execute(query, params)

    def delete(self) -> None:
        query = f'DELETE FROM "{self.__class__.__name__}" WHERE id = %s'
        params = [self.id]
        self.conn.execute(query, params)


class Department(MODEL):
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Department(id={self.id}, name={self.name}, phone={self.phone})"


class Employee(MODEL):
    def __init__(self, id, account, department, phone):
        self.id = id
        self.account = account
        self.department = department
        self.phone = phone

    def __str__(self):
        return f"Employee(id={self.id}, account={self.account}, department={self.department}, phone={self.phone})"


class Project(MODEL):
    def __init__(self, id, title, department, estimated_end_time, end_time):
        self.id = id
        self.title = title
        self.department = department
        self.estimated_end_time = estimated_end_time
        self.end_time = end_time

    def __str__(self):
        return f"Project(id={self.id}, title={self.title}, department={self.department}, estimated_end_time={self.estimated_end_time}, end_time={self.end_time})"


class Employeeprojectrelation(MODEL):
    def __init__(self, id, employee, project, hours, role):
        self.id = id
        self.employee = employee
        self.project = project
        self.hours = hours
        self.role = role

    def __str__(self):
        return f"Employeeprojectrelation(id={self.id}, employee={self.employee}, project={self.project}, hours={self.hours}, role={self.role})"


class Attendance(MODEL):
    def __init__(self, id, employee, date, in_time, out_time, late_cause=None):
        self.id = id
        self.employee = employee
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.late_cause = late_cause

    def __str__(self):
        return f"Attendance(id={self.id}, employee={self.employee}, date={self.date}, in_time={self.in_time}, out_time={self.out_time}, late_cause={self.late_cause})"


class Salary(MODEL):
    def __init__(self, id, employee, base, tax, insurance, overtime):
        self.id = id
        self.employee = employee
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime

    def __str__(self):
        return f"Salary(id={self.id}, employee={self.employee}, base={self.base}, tax={self.tax}, insurance={self.insurance}, overtime={self.overtime})"


class Payment(MODEL):
    def __init__(self, id,amount, account_number, payment_type, description, date):
        self.id = id
        self.amount = amount
        self.account_number = account_number
        self.payment_type = payment_type
        self.description = description
        self.date = date

    def __str__(self):
        return f"Payment(id={self.id}, amount={self.amount}, account_number={self.account_number}, payment_type={self.payment_type}, description={self.description}, date={self.date})"


class Payslip(MODEL):

    def __init__(self, id, base, tax, insurance, overtime, salary, created, payment):
        self.id = id
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime
        self.salary = salary
        self.created = created
        self.payment = payment

    def __str__(self):
        return f"Payslip(id={self.id}, base={self.base}, tax={self.tax}, insurance={self.insurance}, overtime={self.overtime}, salary={self.salary}, created={self.created}, payment={self.payment})"
