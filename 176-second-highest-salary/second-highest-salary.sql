# Write your MySQL query statement below

#As we need to handle null values the below query doesnot work
-- with second_highest as (
--     select
--     salary as SecondHighestSalary,
--     Dense_rank() Over (order by salary desc) as rnk
--     from Employee
-- )

-- select SecondHighestSalary
-- from second_highest
-- where rnk = 2

#So use this query
Select(
    SELECT DISTINCT salary 
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1) AS SecondHighestSalary