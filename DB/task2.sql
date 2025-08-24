-- 1.
SELECT *
FROM Employees
WHERE First_Name LIKE '%m%';

-- 2.
SELECT *
FROM Employees
WHERE Salary > 60000;

-- 3.
SELECT CONCAT(First_Name, ' ', Last_Name) AS Full_Name, Dept_No
FROM Employees;

-- 4.
SELECT DISTINCT Student_No
FROM Student_Courses
WHERE Grade > 70;

-- 5.
SELECT DISTINCT Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 2;

-- 6.
SELECT First_Name, Last_Name, (Salary * 12) AS Annual_Salary
FROM Employees;

-- 7.
SELECT *
FROM Employees
WHERE Salary > 100000 AND Dept_No = 4;

-- 8.
SELECT *
FROM Employees
WHERE Gender = 'Male';

-- 9.
SELECT *
FROM Employees
WHERE Salary IS NOT NULL AND Bonus IS NULL;

-- 10.
SELECT *
FROM Employees
WHERE SUBSTRING(First_Name, 4, 1) = 'F';

-- 11.
SELECT *
FROM Courses
WHERE Duration > 70;

-- 12.
SELECT MIN(Grade) AS Min_Grade
FROM Student_Courses
WHERE Course_No = 3;

-- 13.
SELECT *
FROM Employees
WHERE Dept_No IN (1, 2);
