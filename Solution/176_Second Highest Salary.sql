SELECT
    IFNULL(
        (SELECT DISTINCT Salary
         FROM Employee
         ORDER By Salary DESC
         LIMIT 1 OFFSET 1),
         NULL
         ) AS SecondHighestSalary
