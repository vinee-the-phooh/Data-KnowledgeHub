--List All the films with their titile and release year
select f.title , f.release_year  from film f

--Show the first 10 customers
select * from customer c 
order by c.create_date asc 
limit 10

-- Retrive all unique movie ratings
select distinct f.rating from film f 

--Find the all active customer
select * from customer c 
where c.active = 1

--List the all staff members and their stores
select s.first_name , s.last_name , s.store_id  from staff s 
