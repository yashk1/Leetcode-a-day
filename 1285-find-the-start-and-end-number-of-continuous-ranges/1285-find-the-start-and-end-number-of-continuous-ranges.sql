# Write your MySQL query statement below
# 
with cte as (
select
    log_id,
    (log_id - row_number() over() )as diff
from logs)

select 
    min(log_id) as start_id,
    max(log_id) as end_id
from cte 
group by diff
