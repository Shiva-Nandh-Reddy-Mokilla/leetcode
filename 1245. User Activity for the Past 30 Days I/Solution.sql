# Write your MySQL query statement below
SELECT activity_date AS day,COUNT(DISTINCT USER_ID) AS active_users 
FROM Activity
WHERE activity_date<'2019-07-28' and activity_date>'2019-06-27'
GROUP BY activity_date