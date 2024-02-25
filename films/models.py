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

class Films(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='Название фильма')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(null=True, blank=True, verbose_name='Описание фильма')
    image = models.ImageField(upload_to='films_images', verbose_name='Постер фильма')
    release_date = models.DateTimeField(verbose_name='Дата выхода фильма')
    score = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Моя оценка фильму')
    director = models.ForeignKey(Directors, on_delete=models.CASCADE, verbose_name="Режиссер фильма")

    class Meta:
        db_table = 'film'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title