from django.urls import path
from catalog_films.views import catalog_films, about

app_name = 'catalog_films'

urlpatterns = [
    path('', catalog_films, name='index'),
    path('about/', about, name='about'),
]