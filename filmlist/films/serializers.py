from rest_framework import serializers
from films.models import Film, Theater, Genre

class FilmSerializer(serializers.ModelSerializer):
    theater_set = serializers.StringRelatedField(many=True)
    genre = serializers.StringRelatedField()
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')

class GenreSerializer(serializers.ModelSerializer):
    film_set = FilmSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'film_set')



class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')

class TheaterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True)

    class Meta:
        model = Theater
        fields = ('id', 'name', 'location', 'films')
