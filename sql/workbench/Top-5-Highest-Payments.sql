Find the top N-th highest payments

select distinct p.amount from payment p 
order by p.amount desc
limit 5
