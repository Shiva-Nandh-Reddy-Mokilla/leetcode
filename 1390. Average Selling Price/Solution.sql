SELECT p.product_id,ifnull(round(SUM(units*price)/sum(units),2),0) AS average_price FROM Prices p
LEFT JOIN UnitsSold u on u.product_id=p.product_id and u.purchase_date between p.start_date and p.end_date
GROUP BY product_id
