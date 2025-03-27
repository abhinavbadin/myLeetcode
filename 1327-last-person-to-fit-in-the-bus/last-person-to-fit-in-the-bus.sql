# Write your MySQL query statement below

#using window function definitely benefits
With CTE as (
    select *,
    Sum(weight) Over(order by turn) as total_weight,
    Rank() Over(order by turn) rnk #just to show case if we are ordering in right direction
    from Queue
)

select person_name
from CTE
where total_weight <=1000
order by total_weight DESC
limit 1