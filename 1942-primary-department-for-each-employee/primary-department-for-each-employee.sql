# Write your MySQL query statement below

#Here the trickiest part is getting ids od people with single record

#Method-1 is Using Union
-- select employee_id, department_id 
-- from Employee
-- where primary_flag = 'Y'
-- Union
-- select employee_id, department_id
-- from Employee
-- group by employee_id
-- having count(employee_id) = 1

#Method-2 is Using Window Function
select employee_id, department_id 
from (
    select *,
    Count(employee_id) over(partition by employee_id) as empCount
    from Employee
)empPartition
where primary_flag = 'Y' #We know this is base but we nee employee with atleast count 1 SO modify from
or empCount = 1