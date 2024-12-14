SELECT name FROM Employee
WHERE id in (
    SELECT managerId FROM Employee
    group by managerId
    having COUNT(managerId)>4
    
)