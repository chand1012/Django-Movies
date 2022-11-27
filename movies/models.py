from django.db import models

# Create your DB schema here.
# See this tutorial for more info: https://docs.djangoproject.com/en/4.1/intro/tutorial02/

class Review(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    movie = models.ForeignKey('Movies', on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.username + " " + str(self.movie) + " " + str(self.rating))

class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    release_date = models.CharField(max_length=20)
    rating = models.ManyToManyField(Review)
    imdb_id = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.title + " " + self.release_date)

class ActorMovies(models.Model):
    imdb_id = models.CharField(max_length=20, null=True)
    actor = models.ForeignKey('Actors', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.imdb_id + " " + self.actor)

class Actors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    actor_id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
