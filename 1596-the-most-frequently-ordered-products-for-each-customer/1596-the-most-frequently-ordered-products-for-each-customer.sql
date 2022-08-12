# Write your MySQL query statement below
# most frewquently ordered product for each customer

#customer_id | most ordered item 
#customer_id | product_id | product_name

select customer_id,
    product_id,
    product_name from (
select 
    o.customer_id,
    p.product_id,
    p.product_name,
    rank() over(partition by o.customer_id order by count(o.order_id) DESC) as rnk
from orders o join products p 
on o.product_id = p.product_id
group by 1,2,3)a
where a.rnk =1

