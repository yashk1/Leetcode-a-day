# Write your MySQL query statement below
# project | most experienced employee\

select project_id, employee_id from(
select 
    p.project_id,
    e.employee_id,
    dense_rank() over(partition by project_id order by experience_years DESC) as rnk
from project p inner join employee e
on p.employee_id = e.employee_id
)a
where a.rnk =1
