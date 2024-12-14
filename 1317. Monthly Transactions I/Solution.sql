SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month, 
    country, 
    COUNT(*) AS trans_count, 
    COUNT(CASE WHEN state='approved' THEN 1 END) AS approved_count, 
    SUM(amount) AS trans_total_amount, 
    SUM(CASE WHEN state="approved" then amount else 0 end) as approved_total_amount
FROM 
    Transactions
GROUP BY 
    MONTH(trans_date),YEAR(trans_date),country;
