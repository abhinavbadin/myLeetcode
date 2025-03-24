# Write your MySQL query statement below
# we can get the forst order date using min
# We need to use our filter on those min filtered records only right, thats why putting that in where clause

Select round(avg(order_date = customer_pref_delivery_date)*100, 2) as immediate_percentage
from Delivery
where (customer_id, order_date) IN (
    select customer_id, min(order_date)
    from Delivery
    group by customer_id
)