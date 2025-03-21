# Write your MySQL query statement below
select contest_id,
Round((count(distinct user_id) / (select count(user_id) from Users))  * 100.0,2) as percentage
From Register
Group by contest_id
order by percentage desc, contest_id 