# Generated by Django 3.2.16 on 2022-11-26 16:13

import csv

from django.db import migrations
from tqdm import tqdm


def add_actor(apps, editor):
    with open('new_actors.tsv', mode ='r', encoding= "utf-8") as file:

       # reading the CSV file
       csv_reader = csv.reader(file, delimiter= "\t")

       for x, line in tqdm(enumerate(csv_reader), total=9938594):
        #skip the first row
        if x == 0:
            continue

        #save the name of the actors
        Actor = apps.get_model('movies', 'Actors')
        ActorMovies = apps.get_model('movies', 'ActorMovies')

        first_name = line[1]
        last_name = ""
        name = first_name.split(" ")
        if len(name) == 2:
            first_name = name[0]
            last_name = name[1]
        elif len(name) > 2:
            last_name = name[-1]
            first_name = " ".join(name[:-1])

        actor = Actor(first_name=first_name, last_name=last_name)
        actor.save()

        actor_movies = line[5].split(",")

        for movie in actor_movies:
            actor_movie = ActorMovies(imdb_id=movie, actor=actor)
            actor_movie.save()

class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20221126_1634'),
    ]

    operations = [
        migrations.RunPython(add_actor),
    ]
