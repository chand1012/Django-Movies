# Generated by Django 3.2.16 on 2022-11-28 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_add_movie'),
    ]

    operations = [
        migrations.RunSQL("""
        DELETE FROM movies_movies WHERE release_date = '\\N';
        """)
    ]