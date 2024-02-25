from django.contrib import admin
from films.models import MovieGenres, Films, Directors


@admin.register(MovieGenres)
class MovieGenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Directors)
class DirectorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

