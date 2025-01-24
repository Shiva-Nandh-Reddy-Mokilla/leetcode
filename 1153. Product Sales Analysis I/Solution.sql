# Write your MySQL query statement below
select product_name,year,price from Sales s1
left join Product p on p.product_id=s1.product_id
