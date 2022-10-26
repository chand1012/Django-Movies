from django.db import models

# Create your DB schema here.
# See this tutorial for more info: https://docs.djangoproject.com/en/4.1/intro/tutorial02/

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.title)

class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.ManyToManyField(User)

    def __str__(self):
        return str(self.title)

class Actors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    actor_id = models.AutoField(primary_key=True)
    movies = models.ManyToManyField(Movies)

    def __str__(self):
        return str(self.title)
