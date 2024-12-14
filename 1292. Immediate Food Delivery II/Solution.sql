select round((sum(order_date=customer_pref_delivery_date)/ COUNT(*))*100,2) as immediate_percentage
from Delivery
    WHERE (customer_id,order_date) in (
        SELECT customer_id, MIN(order_date) 
        FROM Delivery  
        group by customer_id
    )