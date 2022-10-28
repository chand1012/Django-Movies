from django.shortcuts import render

from movies.models import Movies

def movie_list(request):
    objs = Movies.objects.all()
    return render(request, 'index.html', {'objs':objs})

def movie_detail(request, movie_id):
    obj = Movies.objects.get(movie_id=movie_id)
    return render(request, 'movie.html', {'obj':obj})


