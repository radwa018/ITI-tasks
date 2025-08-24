-- 1.
SELECT d.Dept_No, d.Dept_Name, COUNT(e.Emp_no) AS EmpCount
FROM Departments d
JOIN Employees e ON d.Dept_No = e.Dept_No
GROUP BY d.Dept_No, d.Dept_Name
HAVING COUNT(e.Emp_no) > 200;

-- 2.
SELECT e.Emp_no, e.First_Name, e.Last_Name, COUNT(s.Emp_no) AS SalaryChanges
FROM Employees e
JOIN Salaries s ON e.Emp_no = s.Emp_no
GROUP BY e.Emp_no, e.First_Name, e.Last_Name
HAVING COUNT(s.Emp_no) > 3;

-- 3.
SELECT Dept_No, MAX(Salary) AS MaxSalary
FROM Employees
GROUP BY Dept_No;

-- 4.
SELECT d.Dept_No, d.Dept_Name, SUM(e.Salary) AS TotalSalary
FROM Departments d
JOIN Employees e ON d.Dept_No = e.Dept_No
GROUP BY d.Dept_No, d.Dept_Name
HAVING SUM(e.Salary) > 1000000;

-- 5.
SELECT DISTINCT e.Salary
FROM Employees e
JOIN Departments d ON e.Dept_No = d.Dept_No
WHERE d.Dept_Name = 'Finance'
ORDER BY e.Salary DESC
FETCH FIRST 5 ROWS ONLY;

-- 6.
SELECT c.*
FROM Courses c
LEFT JOIN students_course s ON c.Course_no = s.Course_no
WHERE s.Course_no IS NULL;

-- 7.
SELECT s.Student_no, s.Student_Name, SUM(g.Grade) AS TotalGrade
FROM Students s
JOIN students_course g ON s.Student_no = g.Student_no
GROUP BY s.Student_no, s.Student_Name;

-- 8.
FROM Departments d
JOIN Employees e ON d.Dept_No = e.Dept_No
GROUP BY d.Dept_No, d.Dept_Name
HAVING AVG(e.Salary) < 75000;

-- 9.
SELECT s.Student_no, s.Student_Name, SUM(c.Course_Duration) AS TotalHours
FROM Students s
JOIN students_course g ON s.Student_no = g.Student_no
JOIN Courses c ON g.Course_no = c.Course_no
GROUP BY s.Student_no, s.Student_Name
HAVING SUM(c.Course_Duration) > 300;

-- 10.
(
   SELECT DISTINCT Salary
   FROM Employees
   WHERE Salary IS NOT NULL
   ORDER BY Salary DESC
   FETCH FIRST 1 ROW ONLY
)
UNION
(
   SELECT DISTINCT Salary
   FROM Employees
   WHERE Salary IS NOT NULL
   ORDER BY Salary DESC
   OFFSET 1 ROW FETCH NEXT 1 ROW ONLY
);

-- 11.
SELECT e.First_Name || ' ' || e.Last_Name AS FullName, d.Dept_Name
FROM Employees e
JOIN Departments d ON e.Dept_No = d.Dept_No;

-- 12.
SELECT d.Dept_No, d.Dept_Name, e.Emp_no, e.First_Name, e.Last_Name
FROM Departments d
LEFT JOIN Employees e ON d.Dept_No = e.Dept_No;

-- 13.
SELECT s.Student_Name, c.Course_Name, g.Grade
FROM Students s
JOIN students_course g ON s.Student_no = g.Student_no
JOIN Courses c ON g.Course_no = c.Course_no;

-- 14.
SELECT e.First_Name || ' ' || e.Last_Name AS EmployeeName,
       s.First_Name || ' ' || s.Last_Name AS SupervisorName,
       s.*
FROM Employees e
JOIN Employees s ON e.Super_no = s.Emp_no
WHERE e.First_Name LIKE 'B%';

-- 15.
SELECT DISTINCT e.emp_no, e.first_name, e.last_name
FROM employees e, dept_emp d, salaries s
WHERE e.emp_no = d.emp_no AND e.emp_no = s.emp_no
ORDER BY e.emp_no;
