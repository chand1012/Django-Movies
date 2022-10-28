from django.shortcuts import render, redirect

from movies.models import Movies, Actors

def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'index.html', {'movies':movies})

def movie_detail(request, movie_id):
    movie = Movies.objects.get(movie_id=movie_id)
    actors = Actors.objects.filter(movies=movie)
    return render(request, 'movie.html', {'movie':movie, 'actors':actors})

def actor_details(request, actor_id):
    actor = Actors.objects.get(actor_id=actor_id)
    movies = Movies.objects.filter(actors=actor).all()
    return render(request, 'actor.html', {'actor':actor, 'movies':movies})

def actors_list(request):
    actors = Actors.objects.all()
    return render(request, 'actors.html', {'actors':actors})

def index(request):
    return redirect('movie_list')
