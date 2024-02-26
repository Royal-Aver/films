from django.shortcuts import render, redirect

from catalog_films.models import MovieGenres, Directors, Films
from catalog_films.forms import FilmForm

def catalog_films(request):
    genres = MovieGenres.objects.all()
    films = Films.objects.all()

    context = {
        'title': 'Главная страница',
        'genres': genres,
        'films': films,
    }

    return render(request, 'catalog_films/index.html', context)


def about_site(request):

    context = {
        'title': 'О сайте',
    }

    return render(request,'catalog_films/about_site.html', context)


def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = FilmForm()

    context = {
        'title': 'Добавление фильма',
        'form': form,
    }

    return render(request,'catalog_films/add_film.html', context)
