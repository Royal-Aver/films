from django.shortcuts import render
from django.http import HttpResponse

def films(request, film_slug):
    return HttpResponse('Movies here!!!')
