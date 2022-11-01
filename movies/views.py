from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm

from movies.forms.register import NewUserForm
from movies.models import Actors, Movies, Review


def movie_list(request):
    movies = Movies.objects.all()
    return render(request, 'index.html', {'movies':movies})

def movie_detail(request, movie_id):
    movie = Movies.objects.get(movie_id=movie_id)
    actors = Actors.objects.filter(movies=movie)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'movie.html', {'movie':movie, 'actors':actors, 'reviews': reviews})

def actor_details(request, actor_id):
    actor = Actors.objects.get(actor_id=actor_id)
    movies = Movies.objects.filter(actors=actor).all()
    return render(request, 'actor.html', {'actor':actor, 'movies':movies})

def actors_list(request):
    actors = Actors.objects.all()
    return render(request, 'actors.html', {'actors':actors})

def index(request):
    return redirect('movie_list')

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
		review = Review.objects.create(movie=movie, username=request.user.username, rating=int(request.POST['rating'][0]))
		review.save()
		return redirect('movie_detail', movie_id=movie_id)
	return redirect('movie_detail', movie_id=movie_id)
