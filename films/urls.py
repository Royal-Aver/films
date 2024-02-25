from django.urls import path
from films.views import films, about

app_name = 'films'

urlpatterns = [
    path('films/', films, name='films'),
    path('about/', about, name='about'),
]