from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'year_prod', 'genre', 'img_url']
        labels = {'title': 'Film Title',
                  'year_prod': 'Year',
                  'genre': 'Genre',
                  'img_url': 'Image',
                  }
