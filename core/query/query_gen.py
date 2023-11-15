from core.database.database_engines import DatabaseConnectionManager
from core.database.classes import Employee, MODEL, Department
import time


q1 = '''SELECT SUM(total_dept) "total_dept" FROM (
SELECT employee,SUM(base::DECIMAL+tax::DECIMAL+insurance::DECIMAL+overtime::DECIMAL) 
as "total_dept"
FROM "Salary" WHERE  id NOT IN(SELECT id FROM "Payslip")
GROUP BY employee) AS total_depts'''

q2 = '''WITH overtimes AS (
SELECT S.employee, SUM(P.overtime) overtime FROM "Salary" S 
JOIN "Payslip" P ON S.id = P.salary
GROUP BY S.employee HAVING SUM(P.overtime) >= %s)
SELECT SUM(overtime) AS total_overtime FROM overtimes'''

q3 = '''SELECT SUM(base+overtime+tax+insurance) AS total FROM "Salary" WHERE id IN (
SELECT salary FROM "Payslip" WHERE payment IS NOT NULL)'''

q4 = '''SELECT employee, SUM(hours) AS total
FROM "Employeeprojectrelation" WHERE employee = %s
GROUP BY employee'''

q5 = '''SELECT S.employee, SUM(PA.amount)AS total_amount  
FROM "Salary" S JOIN "Payslip" P ON S.id = P.salary
JOIN public."Payment" PA on P.payment = PA.id
GROUP BY S.employee HAVING SUM(PA.amount) > %s'''

q6 = '''WITH emp AS(
SELECT employee, SUM(hours) AS total
FROM "Employeeprojectrelation"
GROUP BY employee)
SELECT employee,emp.total FROM "Employeeprojectrelation" E 
JOIN emp USING(employee) WHERE emp.total = 
(SELECT MAX(total) FROM emp) ORDER BY employee LIMIT 1'''

q7 = '''WITH department_totals AS (
  SELECT DISTINCT D.id AS department_id, SUM(P2.amount) AS total_payment
  FROM "Department" D
  JOIN "Employee" E ON D.id = E.department
  JOIN "Salary" S ON E.id = S.employee
  JOIN "Payslip" P ON S.id = P.salary
  JOIN "Payment" P2 ON P2.id = P.payment
  GROUP BY D.id)
SELECT D.id,D1.total_payment AS max_total 
FROM department_totals D1 JOIN "Department" D ON D.id = D1.department_id
WHERE D1.total_payment = (SELECT MAX(total_payment) FROM department_totals) ORDER BY D.name LIMIT 1'''

q8 = '''WITH CTE AS (
    SELECT
        D.id,
        SUM(P.estimated_end_time - P.end_time) AS delta,
        RANK() OVER (ORDER BY SUM(P.estimated_end_time - P.end_time) DESC) AS delta_rank
    FROM
        "Department" D
        JOIN public."Project" P ON D.id = P.department
    GROUP BY D.id
) SELECT id, delta
FROM CTE
WHERE delta_rank = 1'''

q9 = '''WITH CTE AS (
SELECT E.id, E.account, E.phone,
       (EXTRACT(HOUR FROM A.in_time::TIME) -
       EXTRACT(HOUR FROM %s::TIME)) :: INT * INTERVAL '1 hour'+
       (EXTRACT(MINUTE FROM A.in_time::TIME) -
       EXTRACT(MINUTE FROM %s::TIME)) :: INT * INTERVAL '1 minute'+
       (EXTRACT(SECOND FROM A.in_time::TIME) -
       EXTRACT(SECOND FROM %s::TIME)) :: INT  * INTERVAL '1 second' AS time_diff
FROM "Employee" E JOIN public."Attendance" A ON E.id = A.employee)

SELECT id, SUM(time_diff) as time_diff FROM CTE GROUP BY id ORDER BY time_diff LIMIT 1'''

q10 = '''SELECT E.id FROM "Employee" E
WHERE E.id NOT IN (
SELECT employee FROM "Employeeprojectrelation")'''




def query1(db, q1):
    data = db.execute_without_commit(q1)
    return {"total_dept": float(data.fetchone()[0])}


# Function 2
def query2(db, q2):
    value = input("waiting for input: ")
    data = db.execute_without_commit(q2, params=[int(value)])
    return {"total_overtime": float(data.fetchone()[0])}


# Function 3
def query3(db,q3):
    data = db.execute_without_commit(q3)
    return {"total": data.fetchone()[0]}


# Function 4
def query4(db, q4):
    try:
        value = input("waiting for input: ")
        data = db.execute_without_commit(q4, params=[int(value)])
        return {"total_hours": data.fetchone()[1]}
    except TypeError:
        return {"total_hours": None}


# Function 5
def query5(db, q5):
    value = input("waiting for input: ")
    data = db.execute_without_commit(q5, params=[int(value)])
    result5 = data.fetchall()
    temp_result = []
    for index, value in enumerate(result5):
        temp_result.append(Employee.from_id(value[0]))
        temp_result[index].total = value[1]
        print(temp_result[index])
        print(f"total amount for employee {temp_result[index].id}: {temp_result[index].total}")
    return temp_result


# Function 6
def query6(db, q6):
    data = db.execute_without_commit(q6)
    result6 = data.fetchall()
    id = result6[0][0]
    total_hours = result6[0][1]
    e = Employee.from_id(id)
    e.total_hours = total_hours
    return e


# Function 7
def query7(db, q7):
    data = db.execute_without_commit(q7)
    result7 = data.fetchall()
    id = result7[0][0]
    total = float(result7[0][1])
    d = Department.from_id(id)
    d.total = total
    return d


# Function 8
def query8(db, q8):
    data = db.execute_without_commit(q8)
    result8 = data.fetchone()
    id = result8[0]
    d = Department.from_id(id)
    return d


# Function 9
def query9(db, q9):
    h = input("waiting for input: ")
    data = db.execute_without_commit(q9, [h, h, h])
    result9 = data.fetchone()
    id = result9[0]
    e = Employee.from_id(id)
    return e


# Function 10
def query10(db, q10):
    data = db.execute_without_commit(q10)
    result10 = data.fetchall()
    return {"total": len(result10)}


def run_all_query():
    db = DatabaseConnectionManager()
    MODEL.conn = db
    functions = {
        "query1": query1,
        "query2": query2,
        "query3": query3,
        "query4": query4,
        "query5": query5,
        "query6": query6,
        "query7": query7,
        "query8": query8,
        "query9": query9,
        "query10": query10}
    queries = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    funcstorun = zip(functions,queries)
    for func, queries in funcstorun:
        time.sleep(0.5)
        print(f"\n\n{func.upper()}!\n")
        result = functions[func](db,queries)
        print(result)

