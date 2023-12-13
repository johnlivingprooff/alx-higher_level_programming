-- lists all cities contained in the database hbtn_0d_usa.

USE hbtn_0d_usa;

-- List all cities with corresponding state names
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
