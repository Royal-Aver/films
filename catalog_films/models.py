from django.db import models

class Directors(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Режиссер')
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        db_table = 'director'
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return self.name


class MovieGenres(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Жанр')
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        db_table = 'genre'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title

class Films(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='Название фильма')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='URL')
    description = models.TextField(null=True, blank=True, verbose_name='Описание фильма')
    image = models.ImageField(upload_to='films_images', null=True, blank=True, verbose_name='Постер фильма')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата выхода фильма')
    score = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Моя оценка фильму')
    has_movie_released = models.BooleanField(default=False)
    director = models.ForeignKey(Directors, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Режиссер фильма")
    genre = models.ForeignKey(MovieGenres, on_delete=models.CASCADE, verbose_name="Жанр фильма")

    class Meta:
        db_table = 'film'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title