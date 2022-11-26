# Generated by Django 3.2.16 on 2022-11-25 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_remove_actor'),
    ]

    operations = [
        migrations.RunSQL("""
            CREATE OR REPLACE FUNCTION search_movies(search_text text)
            RETURNS TABLE(movie_id integer, title text, release_date text, imdb_id text) AS $$
            BEGIN
                RETURN QUERY
                SELECT movie_id, title, year, rating, num_reviews, poster_url, imdb_id
                FROM movies_movies
                WHERE title ILIKE '%' || search_text || '%'
                ORDER BY rating DESC;
            END;
            $$ LANGUAGE plpgsql;
        """),
    ]
