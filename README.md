# Group Project: PostgreSQL and Python Interaction

## Overview

This collaborative project aims to familiarize the team with PostgreSQL, Python, and database interactions. The project involves setting up a PostgreSQL database, creating Python classes for data manipulation, loading test data, and implementing various SQL queries using Python.

## Table of Contents

1. [Installation and Setup](#1-installation-and-setup)
   - [1.1 Preparing a Linux Server](#11-preparing-a-linux-server)
   - [1.2 Creating a User for Each Member](#12-creating-a-user-for-each-member)
   - [1.3 Installing PostgreSQL](#13-installing-postgresql)

2. [Building the Database](#2-building-the-database)

3. [Creating Python Classes](#3-creating-python-classes)
   - [3.1 Get Method](#31-get-method)
   - [3.2 Filter Method](#32-filter-method)
   - [3.3 Delete Method](#33-delete-method)
   - [3.4 Save Method](#34-save-method)

4. [Loading Test Data](#4-loading-test-data)

5. [Search in the Database](#5-search-in-the-database)
   - [5.1 Total Debts of the Company for Employee Salaries](#51-total-debts-of-the-company-for-employee-salaries)
   - [5.2 Total Overtime Salary of Employees](#52-total-overtime-salary-of-employees)
   - [5.3 Total Payments of the Company](#53-total-payments-of-the-company)
   - [5.4 Total Hours Worked by an Employee](#54-total-hours-worked-by-an-employee)
   - [5.5 Employees with High Salaries](#55-employees-with-high-salaries)
   - [5.6 Employee with the Most Completed Project Hours](#56-employee-with-the-most-completed-project-hours)
   - [5.7 Department with the Most Paid Salaries](#57-department-with-the-most-paid-salaries)
   - [5.8 Department with the Most Projects Delivered On Time](#58-department-with-the-most-projects-delivered-on-time)
   - [5.9 Employee with the Least Number of Late Entry Days](#59-employee-with-the-least-number-of-late-entry-days)
   - [5.10 Number of Employees Who Never Participated in Projects](#510-number-of-employees-who-never-participated-in-projects)

6. [Project Requirements](#6-project-requirements)

## 1. Installation and Setup

### 1.1 Preparing a Linux Server

- Obtain a Linux server for your group, supporting SSH access.
- No specific service provider is mandated, but consider ease of access.
- The server should facilitate pay-as-you-go usage.

### 1.2 Creating a User for Each Member

- Create a user on the server for each group member.
- Assign SSH keys to enable members to connect at any time.

### 1.3 Installing PostgreSQL

- Install PostgreSQL on your server.
- For each group member, create a user and a database using PostgreSQL.
- Configure PostgreSQL to allow remote access.

## 2. Building the Database

- Utilize pgAdmin and an ERD tool to design and implement the database.
- Define tables for `Department`, `Employee`, `Project`, `EmployeeProjectRelation`, `Attendance`, `Salary`, `Payment`, and `Payslip`.

## 3. Creating Python Classes

- Develop Python classes corresponding to each table.
- Implement methods for `get`, `filter`, `delete`, and `save`.

### 3.1 Get Method

- Search the corresponding table using input arguments.
- If a single match is found, create an object with the information.
- Handle cases where no match or multiple matches are found.

### 3.2 Filter Method

- Similar to the `get` method but can return multiple objects.

### 3.3 Delete Method

- Similar to the `get` method but deletes the database table row associated with the object.

### 3.4 Save Method

- Store the information in the object in the related table.

## 4. Loading Test Data

- Write Python code to load data from `json.sample_data` into the database.
- Utilize the created Python classes and the `save` method for this task.

## 5. Search in the Database

- Implement SQL queries in Python using psycopg2 to retrieve specific information.

### 5.1 Total Debts of the Company for Employee Salaries

- Return unpaid salaries (overtime + insurance + tax + base) in the form of a dict.

### 5.2 Total Overtime Salary of Employees

- Return the total overtime pay (in Tomans) for employees who worked more than a specified number of hours.

### 5.3 Total Payments of the Company

- Return the total payments of the company in the form of a dict.

### 5.4 Total Hours Worked by an Employee

- Return the total hours worked by an employee in the form of a dict.

### 5.5 Employees with High Salaries

- Return a list of employees whose total salary is more than a specified amount.

### 5.6 Employee with the Most Completed Project Hours

- Return the employee object with an additional column named `hours_total`.
- In case of ties, return the employee with an alphabetically smaller username.

### 5.7 Department with the Most Paid Salaries

- Return the department object with an additional column named `total`.
- In case of ties, return the department with an alphabetically smaller name.

### 5.8 Department with the Most Projects Delivered On Time

- Return the department object with an additional column named `total`.
- In case of ties, return the department with an alphabetically smaller name.

### 5.9 Employee with the Least Number of Late Entry Days

- Return the employee

## 6. Project Requirements

Please refer to the [directory structure](#directory-structure) for details on the organization of project files.

### Directory Structure

```plaintext
├── core
│   ├── crudORM
│   │   ├── deletion.py
│   │   ├── insertion.py
│   │   ├── selection.py
│   │   └── updation.py
│   ├── database
│   │   ├── classes.py
│   │   ├── classes_structure.py
│   │   ├── database_engines.py
│   │   └── database_structure.txt
│   │   
│   ├── log
│   └── query
│       ├── QUERY
│       └── query_gen.py
├── main.py
├── temp_data
│   ├── data_sample.json
│   └── read_json.py
└── unit_test
    └── test.py
```
    
    
## License

This project is provided under the terms of the Custom Project License (CPL).

You are free to:
- Use this project for educational and non-commercial purposes.
- Modify the code for personal or non-commercial use.

You are not allowed to:
- Use this project or its code for any commercial purposes without explicit permission from the project author.

If you would like to use this project for commercial purposes, please contact the project author to discuss licensing options.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

For more details, please contact the project author at [Contract](#contact).

© [2023] [Yousof.A.Asadi]
## Contact

For any questions or inquiries, you can contact the project author:

- GitHub: [github.com/Y-A-Asd](https://github.com/Y-A-Asd/)
- Email: yosofasady2@gmail.com
