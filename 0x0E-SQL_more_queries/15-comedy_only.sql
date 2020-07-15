-- lists all Comedy shows
-- comment 2
SELECT 
	tv_shows.title 
	FROM tv_show_genres 
	JOIN tv_shows 
	ON tv_show_genres.show_id = tv_shows.id 
	JOIN tv_genres 
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = "Comedy";
