# Write your MySQL query statement below
with cate as (
    select *,
    Case When income < 20000 then 'Low Salary'
    when income between 20000 and 50000 then 'Average Salary'
    when income > 50000 then 'High Salary'
    end as category
    from Accounts
)

select category, count(category) as accounts_count
from cate
group by category
union all
select "Low Salary", 0 where not exists (select 1 from cate where category = 'Low Salary')
union all
select 'Average Salary', 0 where not exists (select 1 from cate where category = 'Average Salary')
union all
select 'High Salary', 0 where not exists (select 1 from cate where category = 'High Salary')