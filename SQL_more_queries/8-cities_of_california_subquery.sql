-- Lists all cities of california that can be found in the db
SELECT id, name FROM cities WHERE id IN (SELECT name FROM states WHERE name = 'California');
