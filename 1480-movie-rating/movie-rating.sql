# Write your MySQL query statement below
#--------------Query-1---------------------
(select u.name as results 
from Users u 
JOIN MovieRating m 
on u.user_id = m.user_id
group by u.user_id
Order by Count(*) desc, u.name asc
LIMIT 1)

Union all

#--------------Query-2---------------------
(select m.title as results
from Movies m 
JOIN MovieRating mr
on m.movie_id = mr.movie_id
where mr.created_at like '2020-02%'
group by m.movie_id
order by AVG(mr.rating) desc, m.title asc
limit 1 )