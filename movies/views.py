from django.views import generic
from .models import Movie
from .forms import MovieForm
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'movies/home.html')

class MovieListView(generic.ListView):
    model = Movie
    template_name = 'movies/movie_list.html'

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

class MovieCreateView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = '/movies/'  

class MovieUpdateView(generic.UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = '/movies/'  

class MovieDeleteView(generic.DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = '/movies/'