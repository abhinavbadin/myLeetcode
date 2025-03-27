# Write your MySQL query statement

# First thing is try to find the product_id which is below the date
# Next try to find the product_id not in the above and make it default values as 10
WITH cte AS
(SELECT *, RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS r 
FROM Products
WHERE change_date<= '2019-08-16')

SELECT product_id, new_price AS price
FROM cte
WHERE r = 1
UNION
SELECT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM cte)