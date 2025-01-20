from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'), 
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),  
    path('create/', views.MovieCreateView.as_view(), name='movie_create'), 
    path('update/<int:pk>/', views.MovieUpdateView.as_view(), name='movie_update'),  
    path('delete/<int:pk>/', views.MovieDeleteView.as_view(), name='movie_delete'),  
]