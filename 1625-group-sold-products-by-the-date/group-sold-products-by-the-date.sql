# Write your MySQL query statement below
select sell_date, 
Count(distinct product) as num_sold,
group_concat(DISTINCT product order by product ASC separator ',') as products
from Activities
group by sell_date
order by sell_date