--Find all movies released in 2006.

select f.title , f.release_year  from film f 
where f.release_year = '2006'

-- Get all films rated “PG-13”

select f.title , f.rating  from film f 
where f.rating  = 'PG-13'

--Find customers whose last name starts with “S”

select c.last_name , c.first_name  from customer c 
where c.last_name  like 'S%'

--Retrieve all payments greater than $5

select p.amount ,p.customer_id  from payment p 
where p.amount > 5

--Find customers who are not active

select c.first_name,c.last_name ,c.active  from customer c 
where c.active != 1