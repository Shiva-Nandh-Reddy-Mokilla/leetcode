# Write your MySQL query statement below
with cte AS (
    select reports_to,count(employee_id) as reports_count, round(avg(age)) as average_age
    from employees
    where reports_to is not null group by reports_to
)
select c.reports_to as employee_id, e.name,c.reports_count,c.average_age
from cte c
left join employees e
on c.reports_to=e.employee_id
order by employee_id