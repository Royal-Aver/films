from django.urls import path
from catalog_films.views import catalog_films, about_site, add_film

app_name = 'catalog_films'

urlpatterns = [
    path('', catalog_films, name='index'),
    path('about-site/', about_site, name='about_site'),
    path('add-film/', add_film, name='add_film'),
]