-- Inner join
Select cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = state_id;
