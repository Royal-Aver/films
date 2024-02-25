from django.shortcuts import render

from films.models import MovieGenres, Directors

def films(request):
    directors = Directors.objects.all()

    context = {
        'title': 'Главная страница',
        'directors': directors
    }

    return render(request, 'films/index.html', context)


def about(request):
    genres = MovieGenres.objects.all()

    context = {
        'title': 'Главная страница',
        'genres': genres
    }

    return render(request,'films/about.html', context)
