# Write your MySQL query statement below
# Write your MySQL query statement below
With CTE as (
    select requester_id, count(distinct accepter_id) as no_of_friends
    from RequestAccepted
    group by requester_id

Union all
    
    select accepter_id, count(distinct requester_id) as no_of_friends
    from RequestAccepted
    group by accepter_id
),
friend_totals AS (
    SELECT requester_id, SUM(no_of_friends) AS total_friends
    FROM CTE
    GROUP BY requester_id
),
max_friends AS (
    SELECT MAX(total_friends) AS max_count
    FROM friend_totals
)

SELECT ft.requester_id as id, ft.total_friends as num
FROM friend_totals ft
JOIN max_friends mf ON ft.total_friends = mf.max_count;