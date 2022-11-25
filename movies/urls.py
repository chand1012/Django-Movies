"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('movies/', views.index, name='movie_list_plain'),
    path('movies/<int:page>', views.movie_list, name='movie_list'),
    path('actors/', views.actor_redirect, name='actor_list'),
    path('actors/<int:page>', views.actors_list, name='actor_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('actor/<int:actor_id>/', views.actor_details, name='actor_detail'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("review/<int:movie_id>", views.review_request, name="review"),
    path("poster/<str:imdb_id>", views.get_poster, name="poster"),
]
