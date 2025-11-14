Find duplicate records where release_year and rating are the same

select f.release_year, f.rating,count(*) as frequency from film f
group by f.release_year, f.rating
having count(*) > 1 

