SELECT contest_id, round(COUNT(*)*100/(select count(*) from Users),2) AS percentage FROM Register r
JOIN Users u USING(user_id)
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC