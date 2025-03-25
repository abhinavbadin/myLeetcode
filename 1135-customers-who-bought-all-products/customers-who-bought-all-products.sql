# Write your MySQL query statement below
# Group by the customer_id so then we can count unique products keys for each customer_id 
# then count keys in product if they are equal the done  
select customer_id
from Customer 
group by customer_id
having count(distinct product_key) = (SELECT COUNT(product_key) FROM Product)