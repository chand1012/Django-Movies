from django.shortcuts import render
from django.http import HttpResponse

def movie_list(request):
    return render(request, 'index.html')

def movie_detail(request, pk):
    return HttpResponse('Movie Detail')


