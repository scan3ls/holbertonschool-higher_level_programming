-- lists all shows w/ at least one genre linked
-- comment 2
SELECT
	tv_shows.title
	,tv_show_genres.genre_id
	FROM tv_shows, tv_show_genres
	WHERE tv_show_genres.show_id = tv_shows.id
	ORDER BY
		tv_shows.title
		,tv_show_genres.genre_id
