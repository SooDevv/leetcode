Select a.name as Employee
from Employee as a join Employee as b
    on a.ManagerId = b.Id
where a.Salary > b.Salary