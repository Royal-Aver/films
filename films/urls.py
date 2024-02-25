from django.urls import path
from films.views import films

app_name = 'films'

urlpatterns = [
    path('films/<slug:film_slug>/', films, name='films'),
]