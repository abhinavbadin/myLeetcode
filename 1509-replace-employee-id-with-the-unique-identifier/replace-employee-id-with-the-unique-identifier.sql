# Write your MySQL query statement below
select u.unique_id, e.name 
from EmployeeUNI u
right Join Employees e ON
e.id = u.id
