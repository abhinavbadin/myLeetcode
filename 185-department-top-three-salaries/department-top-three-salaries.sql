# Write your MySQL query statement below
with employee_ranks as (
    select d.id,
    d.name as Department,
    salary as Salary,
    e.name as Employee,
    Dense_Rank() Over(Partition by d.id order by salary desc) as rnk
    from Department d
    JOIN Employee e 
    ON d.id = e.departmentId
)

select Department, Employee, Salary 
from employee_ranks
where rnk <= 3