-- lists all genres and number of shows
-- comment 2
SELECT
	tv_genres.name 'genre'
	,COUNT(tv_show_genres.genre_id) 'number_of_shows'
	FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_show_genres.genre_id = tv_genres.id
	GROUP BY genre
	ORDER BY
		number_of_shows DESC;
