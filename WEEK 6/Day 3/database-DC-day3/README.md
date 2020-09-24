# database-DC-day3
 
-- create table daniel(
-- id serial primary key,
-- favorite_food int REFERENCES fav_food(id),
-- favorite_movie int references fav_movies(id) 
-- )


-- create table fav_food(
-- id serial primary key,
-- name text
-- )

-- create table fav_movies(
-- id serial primary key,
-- name text
-- )

-- insert into fav_movies (name)
-- values
-- ('Zorro'),
-- ('Tom and Jerry'),
-- ('Blood Diamond')

-- insert into fav_food (name)
-- values
-- ('sushi'),
-- ('pizza'),
-- ('shnitzel')

-- alter table daniel add name text

-- select daniel.name, fav_food.name, fav_movies.name
-- from daniel
-- join fav_food
-- on daniel.id = fav_food.id
-- join fav_movies
-- on daniel.id = fav_movies.id
