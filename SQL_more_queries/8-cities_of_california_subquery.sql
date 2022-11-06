-- Lists all cities of california that can be found in the db
SELECT id, name FROM cities WHERE states_id IN (SELECT name FROM states WHERE name = 'California');
