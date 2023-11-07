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

class Employee(Base):
    __tablename__ = 'Employee'
    id = Column(Integer, primary_key=True)
    account = Column(String(255), nullable=False)
    department = Column(Integer, ForeignKey('Department.id'))
    phone = Column(String(20))
    department_id = relationship('Department', back_populates='employees')

class Project(Base):
    __tablename__ = 'Project'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    department = Column(Integer, ForeignKey('Department.id'))
    estimated_end_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    department_id = relationship('Department', back_populates='projects')

class Employeeprojectrelation(Base):
    __tablename__ = 'Employeeprojectrelation'
    id = Column(Integer, primary_key=True)
    employee = Column(Integer, ForeignKey('Employee.id'))
    project = Column(Integer, ForeignKey('Project.id'))
    hours = Column(Integer)
    role = Column(String(255))
    employee_id = relationship('Employee', back_populates='project_relations')
    project_id = relationship('Project', back_populates='employee_relations')

class Attendance(Base):
    __tablename__ = 'Attendance'
    id = Column(Integer, primary_key=True)
    employee = Column(Integer, ForeignKey('Employee.id'))
    date = Column(Date)
    in_time = Column(Time)
    out_time = Column(Time)
    late_cause = Column(Text)
    employee_id = relationship('Employee', back_populates='attendances')

class Salary(Base):
    __tablename__ = 'Salary'
    id = Column(Integer, primary_key=True)
    employee = Column(Integer, ForeignKey('Employee.id'))
    base = Column(DECIMAL)
    tax = Column(DECIMAL)
    insurance = Column(DECIMAL)
    overtime = Column(DECIMAL)
    employee_id = relationship('Employee', back_populates='salary')

class Payment(Base):
    __tablename__ = 'Payment'
    id = Column(Integer, primary_key=True)
    amount = Column(DECIMAL)
    account_number = Column(String(255))
    payment_type = Column(String(255))
    description = Column(Text)
    date = Column(Date)

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




