from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.db import connection

from movies.forms.register import NewUserForm
from movies.models import Actors, Movies, Review, ActorMovies
from movies.util.moviedb import get_movie_poster_url
from movies.util.parse import parse_movies


def movie_list(request, page=1):
	pages = Paginator(Movies.objects.all().order_by('release_date'), 10)
	prev_page = page - 1
	next_page = page + 1
	if page == 1:
		prev_page = 1
	return render(request, 'index.html', {'movies':pages.page(page), 'prev_page': prev_page, 'next_page': next_page})

def movie_detail(request, movie_id):
	movie = Movies.objects.get(movie_id=movie_id)
	actor_ids = ActorMovies.objects.filter(imdb_id=movie.imdb_id).all()
	actors = Actors.objects.filter(actor_id__in=actor_ids).all()
	reviews = Review.objects.filter(movie=movie)
	return render(request, 'movie.html', {'movie':movie, 'actors':actors, 'reviews': reviews})

def actor_details(request, actor_id):
	actor = Actors.objects.get(actor_id=actor_id)
	am = ActorMovies.objects.filter(actor_id=actor_id).all()
	movies = []
	for x in am:
		try:
			movies.append(Movies.objects.get(imdb_id=x.imdb_id))
		except Movies.DoesNotExist:
			pass
	return render(request, 'actor.html', {'actor':actor, 'movies':movies})

def actors_list(request, page=1):
	pages = Paginator(Actors.objects.all().order_by('actor_id'), 20)
	prev_page = page - 1
	next_page = page + 1
	if page == 1:
		prev_page = 1
	return render(request, 'actors.html', {'actors':pages.page(page), 'prev_page': prev_page, 'next_page': next_page})

def index(request):
    return redirect('movie_list', 1)

def actor_redirect(request):
	return redirect('actor_list', 1)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def review_request(request, movie_id):
	if not request.user.is_authenticated:
		messages.error(request, "You must be logged in to review a movie.")
		return redirect("login")
	movie = Movies.objects.get(movie_id=movie_id)
	if request.method == "POST":
		reviewExists = Review.objects.filter(movie=movie, user=request.user).exists()
		if reviewExists:
			messages.error(request, "You have already reviewed this movie.")
			return redirect("movie_detail", movie_id)
		review = Review.objects.create(movie=movie, username=request.user.username, rating=int(request.POST['rating'][0]))
		review.save()
		return redirect('movie_detail', movie_id=movie_id)
	return redirect('movie_detail', movie_id=movie_id)

def get_poster(request, imdb_id):
	poster_url = get_movie_poster_url(imdb_id)
	if poster_url:
		return redirect(poster_url)
	return HttpResponseNotFound()

def search_movies(request):
	movies = []
	query = False
	if request.GET.get('q'):
		query = True
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM search_movies(LOWER(%s)) ORDER BY release_date ASC", [request.GET['q']])
			movies = cursor.fetchall()
	movies = parse_movies(movies)
	print(movies)
	return render(request, 'search.html', {'results':movies, 'query':query})
	
def add_movie(request):
	if not request.user.is_authenticated:
		messages.error(request, "You must be logged in to add a movie.")
		return redirect("login")
	if request.method == "POST":
		with connection.cursor() as cursor:
			cursor.execute("CALL insert_movie(%s, %s, %s)", [request.POST['title'], request.POST['release_date'], request.POST['imdb_id']])
			messages.info(request, "Movie added successfully.")
	return render(request, 'add.html')

def delete_movie(request):
	if not request.user.is_authenticated:
		messages.error(request, "You must be logged in to delete a movie.")
		return redirect("login")
	if not request.user.is_superuser:
		messages.error(request, "You must be an admin to delete a movie.")
		return redirect("index")
	if request.GET.get('movie_id'):
		movie = Movies.objects.get(movie_id=request.GET['movie_id'])
		movie.delete()
		messages.info(request, "Movie deleted successfully.")
	else:
		messages.error(request, "No movie selected.")
		
	return redirect('movie_list', 1)
