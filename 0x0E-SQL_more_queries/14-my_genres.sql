-- list all genres of the show Dexter
-- comment 2
SELECT DISTINCT
	tv_genres.name 'name'
	FROM tv_genres, tv_shows
	RIGHT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_shows.title = "Dexter"
	ORDER BY
		name;
