# Write your MySQL query statement below
select MIN(ABS(p1.x - p2.x)) as shortest
from point p1
         join point p2
              on p1.x != p2.x
