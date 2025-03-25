# Write your MySQL query statement below

#We need to use subquery because the aggreagtion is only on id, year we want on quantity and price too right
-- select product_id, year as first_year, quantity, price
-- from Sales 
-- where (product_id, year) in (
--     select product_id, min(year)
--     from Sales 
--     group by product_id)

#Suppose for the follow up we want the second year then 

with ranked_sales as(
    select product_id, 
    year,
    quantity,
    price,
    RANK() over(Partition by product_id order by year) as rnk
    from Sales 
)
SELECT product_id, year AS first_year, quantity, price
FROM ranked_sales
WHERE rnk = 1;