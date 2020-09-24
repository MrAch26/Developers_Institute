-- create table student(
-- student_id SERIAL primary key,
-- first_name varchar(100),
-- last_name varchar(200),
-- birth_date timestamp
-- )
-- cmd+shift+/ un-comment

insert into student (first_name, last_name, birth_date)
values
('Marc', 'Dupont', '1998-11-02 00:00:00'),
('Yoan', 'Durant', '2010-03-12 00:00:00'),
('Lea', 'Martin', '1987-07-24 00:00:00'),
('Sarah', 'Benichou', '1996-04-07 00:00:00'),
('lea', 'Dupont', '2003-06-14 00:00:00'),
('Omer', 'Simpson', '1980-02-10 00:00:00')
-- ALTER TABLE student RENAME COLUMN student_id TO id;
-- insert into student(first_name,last_name, birth_date)
-- values 
-- ('Julien','Cohen', '1992-09-08 00:00:00'),
-- ('Lise','Nakache', '1992-04-02 00:00:00')
-- ('Adam','Ziri', '1997-09-08 00:00:00')


-- select * from student
-- select first_name,last_name from student
-- select first_name,last_name from student where student_id  = 2
-- select first_name,last_name from student 
-- where first_name = 'Marc' and last_name = 'Dupont'
-- select first_name,last_name from student 
-- where first_name = 'Marc' or last_name = 'Dupont'
-- select first_name,last_name from student 
-- where first_name like '%a%'
-- select first_name,last_name from student 
-- where first_name like 'A%'
-- select first_name,last_name from student 
-- where first_name like '%a'
-- SELECT first_name FROM student WHERE first_name LIKE '%a_'
-- select first_name,last_name from student where id  = 1 or id = 3
-- select first_name ,last_name, birth_date from student where birth_date >= '2000-01-01 00:00:00'


