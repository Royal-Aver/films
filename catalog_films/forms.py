from django import forms
from catalog_films.models import Films

class FilmForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ('title', 'description', 'image', 'genre')

    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField(required=False)
    genre = forms.CharField()