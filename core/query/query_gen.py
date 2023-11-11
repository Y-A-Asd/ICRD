from core.database.database_engines import DatabaseConnectionManager
from core.database.classes import Employee,MODEL,Department
db = DatabaseConnectionManager()

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

q9 = '''SELECT E.id, E.account, E.phone,
       (EXTRACT(HOUR FROM A.in_time::TIME) - 
       EXTRACT(HOUR FROM %s::TIME)) :: INT || ':' ||
       (EXTRACT(MINUTE FROM A.in_time::TIME) - 
       EXTRACT(MINUTE FROM %s::TIME)) :: INT || ':' ||
       (EXTRACT(SECOND FROM A.in_time::TIME) - 
       EXTRACT(SECOND FROM %s::TIME)) :: INT AS time_diff
FROM "Employee" E
JOIN public."Attendance" A ON E.id = A.employee'''

q10 = '''SELECT E.id FROM "Employee" E
WHERE E.id NOT IN (
SELECT employee FROM "Employeeprojectrelation")'''



MODEL.conn = db


# data = db.execute_without_commit(q1)
# result1={"total_dept": float(data.fetchone()[0])}
# print(result1)
#
# data = db.execute_without_commit(q2,params=[int(input("enter value: "))])
# result2={"total_overtime": float(data.fetchone()[0])}
# print(result2)
#
# data = db.execute_without_commit(q3)
# result3={"total": data.fetchone()[0]}
# print(result3)
#
# try:
#     data = db.execute_without_commit(q4,params=[int(input("enter value: "))])
#     result4={"total_hours": data.fetchone()[1]}
#     print(result4)
# except TypeError:
#     print({"total_hours": None})
#
#Todo :list of obj
# data = db.execute_without_commit(q5,params=[int(input("enter value: "))])
# result5= data.fetchall()
# temp_result = []
# for i in result5:
#     temp_result.append({i[0]:float(i[1])})
# print(temp_result)
#
# data = db.execute_without_commit(q6)
# result6=data.fetchall()
# id = result6[0][0]
# total_hours = result6[0][1]
# e = Employee.from_id(id)
# e.total_hours = total_hours
# print(e)
#
# data = db.execute_without_commit(q7)
# result7=data.fetchall()
# id = result7[0][0]
# total = float(result7[0][1])
# d = Department.from_id(id)
# d.total = total
# print(d)
#
# data = db.execute_without_commit(q8)
# result8=data.fetchone()
# id = result8[0]
# d = Department.from_id(id)
# print(d)

h=input("enter value: ")
data = db.execute_without_commit(q9,[h,h,h])
result9=data.fetchall()
print(result9)