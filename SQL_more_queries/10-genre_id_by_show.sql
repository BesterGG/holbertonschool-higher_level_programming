-- import the database dump from mysql sv
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id;

