from django.shortcuts import render

from catalog_films.models import MovieGenres, Directors, Films

def catalog_films(request):
    genres = MovieGenres.objects.all()
    films = Films.objects.all()

    context = {
        'title': 'Главная страница',
        'genres': genres,
        'films': films,
    }

    return render(request, 'catalog_films/index.html', context)


def about(request):
    genres = MovieGenres.objects.all()

    context = {
        'title': 'Главная страница',
        'genres': genres
    }

    return render(request,'catalog_films/about.html', context)
