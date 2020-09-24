1-select * from actors order by actor_id limit 4
2- select * from actors where actor_id < 5 order by last_name desc
-- The actors that have the letter 'e' in their first_name
3-select * from actors where first_name like '%e%'
4-select * from actors where number_oscars > 5