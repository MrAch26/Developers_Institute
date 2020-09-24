# database-exe-day2
 
-- EXE1 -- xp - day2 

-- update student
-- set first_name = 'Lea'
-- where id = 5

-- update student
-- set birth_date = '1998-11-02 00:00:00'
-- where last_name = 'Dupont'

-- DELETE FROM student WHERE id = 5;

-- SELECT COUNT(id)
-- FROM student

-- SELECT COUNT(id)
-- FROM student
-- where birth_date > '2000/01/01 00:00:00'

-- ALTER TABLE student ADD COLUMN math_grade int;

-- update student
-- set math_grade = 80
-- where id = 1

-- update student
-- set math_grade = 90
-- where id = 2 or id = 4 

-- update student set math_grade = 100 where id = 6

-- select count(id) from student where math_grade > 83

-- insert into student (first_name, last_name, birth_date, math_grade)
-- values
-- ('Omer', 'Simpson', (select birth_date from student where id = 6), 70 )


-- SELECT first_name, last_name, COUNT(math_grade) AS total_grade
-- FROM student 
-- GROUP BY first_name, last_name


-- SELECT SUM(math_grade)
-- FROM student 

# XP GOLD - day 2 

-- select * from customer

-- select concat(first_name,' ',last_name) AS FullName from customer;

-- select distinct create_date from customer 

-- select * from customer order by first_name desc

-- select * from film 
-- select film_id, description, release_year, rental_rate from film order by rental_rate asc

-- select address, district, phone from address where district = 'Texas'

-- select * from film where film_id = 15 or film_id = 150

--  favorite movie --
-- select * from film where film_id = 1000 -- Zorro 

-- select film.film_id, film.title, film.description,  film.length, film.rental_rate
-- from film 
-- join inventory 
-- on film.film_id = inventory.film_id
-- where film.film_id = 1000

-- select * from film where min(rental_rate) as low_price limit 10
-- SELECT * FROM film
-- WHERE
-- 	rental_rate = (SELECT MIN(rental_rate) FROM film)
-- limit 10

-- SELECT * FROM film
-- ORDER BY title 
-- OFFSET 10 ROWS 
-- FETCH FIRST 10 ROW ONLY; 


-- select customer.customer_id, first_name, amount, payment_date
-- from customer
-- join payment
-- on customer.customer_id = payment.customer_id
-- order by customer_id

-- select customer.customer_id, staff.first_name, customer.first_name, amount, payment_date
-- from customer c
-- join payment p
-- on customer.customer_id = payment.customer_id
-- join staff as s
-- on payment.staff_id = staff.staff_id 
-- order by staff.staff_id


-- SELECT film.film_id, film.title, inventory_id
-- FROM film
-- LEFT JOIN inventory 
-- ON inventory.film_id = film.film_id
-- WHERE inventory.film_id IS NULL
-- ORDER BY title;





