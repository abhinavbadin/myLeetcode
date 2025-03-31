# Write your MySQL query statement below
select 
    case 
        when id % 2 = 1 AND id+1 in (select id from Seat) Then id+1
        when id % 2 = 0 Then id-1
        Else id
    End as id,
    student
from Seat
Order by id