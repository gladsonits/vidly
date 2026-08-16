from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()

    return render(request, 'movies_index.html', {'movies': movies})


def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies_detail.html', {'movie': movie})
