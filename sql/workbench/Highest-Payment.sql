Find the highest amount from Payment table

select max(p.amount) as Maxamount from payment p 

Find the highest amount with customer id who made the payment from Payment table

select p.amount as Maxamount , p.customer_id from payment p 
Order by p.amount DESC
Limit 1