-- lists all cities contained in the database hbtn_0d_usa.
-- List all cities with corresponding state names
SELECT cities.id, cities.name, states.name AS 'state_name'
FROM states INNER JOIN cities
ON states.id = cities.state_id;
