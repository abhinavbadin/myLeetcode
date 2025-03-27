# Write your MySQL query statement below
#we can use lead here which checks next row values 
#Create a temp table for that using Cte and then check where a single row in 3 columns equal 
with temp_cte as (
select 
num,
LEAD(num,1) Over(order by id) as l1,
LEAD(num,2) Over(order by id) as l2 
from Logs )

select distinct num as ConsecutiveNums 
from temp_cte
where num = l1 and l1 = l2