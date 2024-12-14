SELECT s.user_id , ROUND(COUNT(CASE WHEN action='confirmed' THEN 1 END)/COUNT(*),2) AS confirmation_rate FROM Signups s
LEFT JOIN Confirmations c USING(user_id)
GROUP BY s.user_id
ORDER BY confirmation_rate ASC