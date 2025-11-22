'''
Problem Statement: 

Table: Employee

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference columns) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. It also contains the ID of their department.
 

Table: Department

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table. It is guaranteed that department name is not NULL.
Each row of this table indicates the ID of a department and its name.
 

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in any order.

Problem Type: Medium

Problem Link: https://leetcode.com/problems/department-highest-salary


'''

WITH CTE AS (SELECT e.id as Employee_Id,e.name as Employee_Name,e.salary,e.departmentId as departmentId,d.name as Department_Name
            FROM Employee AS e LEFT JOIN Department AS d on e.departmentId = d.id),

CTE2 AS (SELECT *,DENSE_RANK() OVER(PARTITION BY Department_Name ORDER BY salary desc) as '_Rank'
        FROM CTE)

SELECT Department_Name as Department, Employee_Name as Employee, salary as Salary
FROM CTE2
WHERE _Rank = 1;


