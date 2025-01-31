from django.urls import path
from .views import (
    home,
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)