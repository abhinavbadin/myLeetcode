# Write your MySQL query statement below
#Simple first try to understand whats going inside
#We need groupBY and having clause because its clearly evident. 
#after doing this its giving just mID but name as DAN.
#but we need to match that id with id and get the name from their. This is where i got idea of e1.id = e2.managerID
select e1.name 
from Employee e1
JOIN Employee e2 on e1.id = e2.managerID
group by e2.managerID
having count(e2.managerId) >=5