# Write your MySQL query statement below
DELETE p
from Person p 
JOIN Person p2
ON p.email = p2.email and p.id > p2.id