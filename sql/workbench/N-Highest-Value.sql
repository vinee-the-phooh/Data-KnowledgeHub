Find the N th highest amount from the Payment table. 

select distinct p.amount, p.customer_id  from payment p 
order by p.amount desc
offset N-1 limit 1