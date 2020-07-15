-- lists all cities ocontained in the database
-- comment 2
SELECT
    cities.id
	,cities.name
	,states.name
    FROM cities, states
	WHERE cities.state_id = states.id
    ORDER BY id;
