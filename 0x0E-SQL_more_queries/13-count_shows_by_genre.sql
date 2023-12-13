-- List genres with the number of shows linked
SELECT tv_show_genres.genre_id AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;