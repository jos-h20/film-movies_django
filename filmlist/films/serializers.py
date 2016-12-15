from rest_framework import serializers
from films.models import Film, Theater, Genre
from django.contrib.auth.models import User

class FilmSerializer(serializers.ModelSerializer):
    # theater_set = serializers.StringRelatedField(many=True)
    # genre = serializers.StringRelatedField()
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Film
        fields = ('title', 'year_prod')

class UserSerializer(serializers.ModelSerializer):
    films = FilmSerializer(allow_null=True, many=True)

    # films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'films')

class GenreSerializer(serializers.ModelSerializer):
    film_set = FilmSerializer(allow_null=True, many=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'film_set')
        depth=2

class GenreWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'film_set')



class FilmWriteSerializer(serializers.ModelSerializer):
    # genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')
        # depth=1

class TheaterSerializer(serializers.ModelSerializer):
    # films = serializers.PrimaryKeyRelatedField(queryset=Film.objects.all(), allow_null=True, many=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Theater
        fields = ('id', 'name', 'location', 'films', 'owner')
