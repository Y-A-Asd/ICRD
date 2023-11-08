from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP, Date, Time, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from core.database.engine import engine


Base = declarative_base()

class Department(Base):
    __tablename__ = 'Department'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(20))

    def __init__(self,id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name}, phone={self.phone})"

class Employee(Base):
    __tablename__ = 'Employee'
    id = Column(Integer, primary_key=True)
    account = Column(String(255), nullable=False)
    department = Column(Integer, ForeignKey('Department.id'))
    phone = Column(String(20))
    department_id = relationship('Department', back_populates='employees')
    def __init__(self, id, account, department, phone):
        self.id = id
        self.account = account
        self.department = department
        self.phone = phone

    def __repr__(self):
        return f"Employee(id={self.id}, account={self.account}, department={self.department}, phone={self.phone})"
class Project(Base):
    __tablename__ = 'Project'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    department = Column(Integer, ForeignKey('Department.id'))
    estimated_end_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    department_id = relationship('Department', back_populates='projects')

    def __init__(self, id, title, department, estimated_end_time, end_time):
        self.id = id
        self.title = title
        self.department = department
        self.estimated_end_time = estimated_end_time
        self.end_time = end_time

    def __repr__(self):
        return f"Project(id={self.id}, title={self.title}, department={self.department}, estimated_end_time={self.estimated_end_time}, end_time={self.end_time})"
class Employeeprojectrelation(Base):
    __tablename__ = 'Employeeprojectrelation'
    id = Column(Integer, primary_key=True)
    employee = Column(Integer, ForeignKey('Employee.id'))
    project = Column(Integer, ForeignKey('Project.id'))
    hours = Column(Integer)
    role = Column(String(255))
    employee_id = relationship('Employee', back_populates='project_relations')
    project_id = relationship('Project', back_populates='employee_relations')

    def __init__(self, id, employee, project, hours, role):
        self.id = id
        self.employee = employee
        self.project = project
        self.hours = hours
        self.role = role

    def __repr__(self):
        return f"Employeeprojectrelation(id={self.id}, employee={self.employee}, project={self.project}, hours={self.hours}, role={self.role})"

class Attendance(Base):
    __tablename__ = 'Attendance'
    id = Column(Integer, primary_key=True)
    employee = Column(Integer, ForeignKey('Employee.id'))
    date = Column(Date)
    in_time = Column(Time)
    out_time = Column(Time)
    late_cause = Column(Text)
    employee_id = relationship('Employee', back_populates='attendances')

    def __init__(self, id,employee, date, in_time, out_time, late_cause):
        self.id = id
        self.employee = employee
        self.date = date
        self.in_time = in_time
        self.out_time = out_time
        self.late_cause = late_cause

    def __repr__(self):
        return f"Attendance(id={self.id}, employee={self.employee}, date={self.date}, in_time={self.in_time}, out_time={self.out_time}, late_cause={self.late_cause})"

class Salary(Base):
    __tablename__ = 'Salary'
    id = Column(Integer, primary_key=True)
    employee = Column(Integer, ForeignKey('Employee.id'))
    base = Column(DECIMAL)
    tax = Column(DECIMAL)
    insurance = Column(DECIMAL)
    overtime = Column(DECIMAL)
    employee_id = relationship('Employee', back_populates='salary')

    def __init__(self, id, employee, base, tax, insurance, overtime):
        self.id = id
        self.employee = employee
        self.base = base
        self.tax = tax
        self.insurance = insurance
        self.overtime = overtime

    def __repr__(self):
        return f"Salary(id={self.id}, employee={self.employee}, base={self.base}, tax={self.tax}, insurance={self.insurance}, overtime={self.overtime})"

class Payment(Base):
    __tablename__ = 'Payment'
    id = Column(Integer, primary_key=True)
    amount = Column(DECIMAL)
    account_number = Column(String(255))
    payment_type = Column(String(255))
    description = Column(Text)
    date = Column(Date)

    def __init__(self,id,amount, account_number, payment_type, description, date):
        self.id = id
        self.amount = amount
        self.account_number = account_number
        self.payment_type = payment_type
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Payment(id={self.id}, amount={self.amount}, account_number={self.account_number}, payment_type={self.payment_type}, description={self.description}, date={self.date})"

    def __init__(self, amount, account_number, payment_type, description, date):
        self.amount = amount
        self.account_number = account_number
        self.payment_type = payment_type
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Payment(id={self.id}, amount={self.amount}, account_number={self.account_number}, payment_type={self.payment_type}, description={self.description}, date={self.date})"

class Payslip(Base):
    __tablename__ = 'Payslip'
    id = Column(Integer, primary_key=True)
    base = Column(DECIMAL)
    tax = Column(DECIMAL)
    insurance = Column(DECIMAL)
    overtime = Column(DECIMAL)
    salary = Column(DECIMAL)
    created = Column(Date)
    payment = Column(Integer, ForeignKey('Payment.id'))
    payment_id = relationship('Payment', back_populates='payslips')

    def __init__(self, id,base, tax, insurance, overtime, salary, created, payment):
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




