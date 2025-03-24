# Write your MySQL query statement below
#What i have learnt 
#EXTRACT(part from date)
#Countif, sumif they both are wriiten in the same way COUNT/SUM(CASE WHEN <Condition> THEN 1/something END)

select DATE_FORMAT(trans_date, '%Y-%m') as month,
country,
count(state) as trans_count,
count(Case when state = 'approved' Then 1 END) as approved_count,
sum(amount) as trans_total_amount,
COALESCE(sum(Case when state = 'approved' then amount END),0) as approved_total_amount
from Transactions
group by country, month