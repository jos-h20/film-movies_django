# from rest_framework import generics

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from films.models import Film, Theater, Genre
from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer, FilmWriteSerializer

# from . import serializers
# from . import models

def home(request):
    return render(request, 'home.html')

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', { 'films': films })

def film_detail(request, pk):
    film = Film.objects.get(pk=pk)
    theaters = film.theater_set
    return render(request, 'films/film_detail.html', {'film': film, 'theaters': theaters})

def theater_list(request):
    theater = Theater.objects.all()
    return render(request, 'films/theater_list.html', {'theaters': theater})

def theater_detail(request, pk):
    theater = Theater.objects.get(pk=pk)
    films = theater.films

    return render(request, 'films/theater_detail.html', {'theater': theater, 'films': films})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'films/genre_list.html', {'genres': genres})

def genre_detail(request, pk):
    genre = Genre.objects.get(pk=pk)
    return render(request, 'films/genre_detail.html', {'genre': genre})




@api_view(['GET', 'POST'])
def api_film_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        films = Film.objects.all()
        serializedFilm = FilmSerializer(films, many=True)
        return Response(serializedFilm.data)

    elif request.method == 'POST':
        serializedFilm = FilmWriteSerializer(data=request.data)
        if serializedFilm.is_valid():
            serializedFilm.save()
            return Response(serializedFilm.data, status=status.HTTP_201_CREATED)
        return Response(serializedFilm.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_film_detail(request, pk, format=None):
    """
    Retrieve, update or delete a film instance.
    """
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def api_theater_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        theaters = Theater.objects.all()
        serializer = TheaterSerializer(theaters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_theater_detail(request, pk, format=None):
    """
    Retrieve, update or delete a theater instance.
    """
    try:
        theater = Theater.objects.get(pk=pk)
    except Theater.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TheaterSerializer(theater)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TheaterSerializer(theater, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def api_theater_films(request, pk, format=None):
    """
    Retrieve, update or delete a theater_films instance.
    """
    try:
        theater = Theater.objects.get(pk=pk)
    except Theater.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmSerializer(theater.films.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TheaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        theater.films.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def api_genre_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_genre_detail(request, pk, format=None):
    """
    Retrieve, update or delete a genre instance.
    """
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ListCreateFilm(generics.ListCreateAPIView):
#     queryset = models.Film.objects.all()
#     serializer_class = serializers.FilmSerializer
#
# class RetrieveUpdateDestroyFilm(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Film.objects.all()
#     serializer_class = serializers.FilmSerializer
# Create your views here.
