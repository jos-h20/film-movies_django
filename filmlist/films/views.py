from rest_framework import generics, permissions
from django.shortcuts import render
from films.models import Film, Theater, Genre
from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer, FilmWriteSerializer, GenreWriteSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from films.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
import requests


# class FilmList(APIView):
#     """
#     List all films, or create a new film.
#     """
#     def get(self, request, format=None):
#         films = Film.objects.all()
#         serialized_films = FilmSerializer(films, many=True)
#         return Response(serialized_films.data)
#
#     def post(self, request, format=None):
#         film = FilmSerializer(data=request.data)
#         if film.is_valid():
#             film.save()
#             return Response(film.data, status=status.HTTP_201_CREATED)
#         return Response(film.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class FilmDetail(APIView):
#     """
#     Retrieve, update or delete a film instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Film.objects.get(pk=pk)
#         except Film.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         film = self.get_object(pk)
#         serialized_film = FilmSerializer(film)
#         return Response(serialized_film.data)
#
#     def put(self, request, pk, format=None):
#         film = self.get_object(pk)
#         serialized_film = FilmSerializer(film, data=request.data)
#         if serialized_film.is_valid():
#             serialized_film.save()
#             return Response(serialized_film.data)
#         return Response(serialized_film.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         film = self.get_object(pk)
#         film.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class TheaterList(APIView):
#     """
#     List all theaters, or create a new theater.
#     """
#     def get(self, request, format=None):
#         theaters = Theater.objects.all()
#         serializer = TheaterSerializer(theaters, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = TheaterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class TheaterDetail(APIView):
#     """
#     Retrieve, update, or delete a film instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Theater.objects.get(pk=pk)
#         except Theater.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         theater = self.get_object(pk)
#         serializer = TheaterSerializer(theater)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         theater = self.get_object(pk)
#         serializer = TheaterSerializer(theater, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         theater = self.get_object(pk)
#         theater.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class TheaterFilms(APIView):
#     """
#     Retrieve, update, or delete a theater_film instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Theater.objects.get(pk=pk)
#         except Theater.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         theater = self.get_object(pk)
#         serializer = FilmSerializer(theater.films.all(), many=True)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         theater = self.get_object(pk)
#         serializer = TheaterSerializer(theater, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         theater = self.get_object(pk)
#         theater.films.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class GenreList(APIView):
#     """
#     Retrieve, update or delete a genre instance.
#     """
#     def get(self, request, format=None):
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(genres, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GenreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class GenreDetail(APIView):
#     """
#     Retrieve, update, or delete a film instance.
#     """
#
#     def get_object(self, pk):
#         try:
#             return Genre.objects.get(pk=pk)
#         except Genre.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         genre = self.get_object(pk)
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         genre = self.get_object(pk)
#         serializer = GenreSerializer(genre, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         genre = self.get_object(pk)
#         genre.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)











# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.http import HttpResponse
#
# from films.models import Film, Theater, Genre
# from films.serializers import FilmSerializer, TheaterSerializer, GenreSerializer, FilmWriteSerializer
#
from films.forms import FilmForm

from . import serializers
from . import models
#
def home(request):
    return render(request, 'home.html')

def film_list(request):
    films = Film.objects.all()
    form = FilmForm()
    return render(request, 'films/film_list.html', { 'films': films, 'form':form })

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

def post_film(request):
    films = Film.objects.all()
    form = FilmForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return render(request, 'films/film_list.html', {'films':films})
@api_view(['GET', 'PUT', 'DELETE'])
def film_title(request, format=None):
    """
    Get a list of films that have the word 'hunger' in the title
    """
    if request.method == 'GET':
        payload = {'type': 'movie', 's': 'happy', 'y': '2009'}
        films = requests.get('http://www.omdbapi.com/', params=payload)
        json = films.json()
        a = []
        for key in json['Search']:
            films_dict = {}
            films_dict['title'] = key['Title']
            films_dict['year_prod'] = key['Year']
            a.append(films_dict)
        serializedFilm = FilmSerializer(a, many=True)
        return Response(serializedFilm.data)
#
#
#
# @api_view(['GET', 'POST'])
# def api_film_list(request, format=None):
#     """
#     List all snippets, or create a new film.
#     """
#     if request.method == 'GET':
#         films = Film.objects.all()
#         serializedFilm = FilmSerializer(films, many=True)
#         return Response(serializedFilm.data)
#
#     elif request.method == 'POST':
#         serializedFilm = FilmWriteSerializer(data=request.data)
#         if serializedFilm.is_valid():
#             serializedFilm.save()
#             return Response(serializedFilm.data, status=status.HTTP_201_CREATED)
#         return Response(serializedFilm.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_film_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a film instance.
#     """
#     try:
#         film = Film.objects.get(pk=pk)
#     except Film.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = FilmSerializer(film)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = FilmSerializer(film, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         film.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def api_theater_list(request, format=None):
#     """
#     List all snippets, or create a new film.
#     """
#     if request.method == 'GET':
#         theaters = Theater.objects.all()
#         serializer = TheaterSerializer(theaters, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TheaterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #
# #
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_theater_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a theater instance.
#     """
#     try:
#         theater = Theater.objects.get(pk=pk)
#     except Theater.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TheaterSerializer(theater)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TheaterSerializer(theater, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         theater.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# #
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_theater_films(request, pk, format=None):
#     """
#     Retrieve, update or delete a theater_films instance.
#     """
#     try:
#         theater = Theater.objects.get(pk=pk)
#     except Theater.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = FilmSerializer(theater.films.all(), many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TheaterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         theater.films.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def api_genre_list(request, format=None):
#     """
#     List all snippets, or create a new film.
#     """
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(genres, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = GenreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_genre_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a genre instance.
#     """
#     try:
#         genre = Genre.objects.get(pk=pk)
#     except Genre.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = GenreSerializer(genre)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = GenreSerializer(genre, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         genre.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, permissions.IsAdminUser,)

    def get_serializer_class(self):
            if(self.request.method == 'GET'):
                return FilmSerializer
            return FilmWriteSerializer

    def get(self, request, *args, **kwargs):
        # year_prod = request.GET.get('year_prod', '')
        # title = request.GET.get('title', '')
        # films = Film.objects.filter(title__startswith=title)
        # serialized_films = FilmSerializer(films, many=True)
        # return Response(serialized_films.data)

        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            films = Film.objects.filter(**filter_dict)
            serialized_films = FilmSerializer(films, many=True)
            return Response(serialized_films.data)
        else:
            return Response(FilmSerializer(Film.objects.all(), many=True).data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, permissions.IsAdminUser,)

    def get_serializer_class(self):
            if(self.request.method == 'GET'):
                return FilmSerializer
            return FilmWriteSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            films = Film.objects.filter(**filter_dict)
            serialized_films = FilmSerializer(films, many=True)
            return Response(serialized_films.data)
        else:
            return Response(FilmSerializer(Film.objects.all(), many=True).data)

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = serializers.TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = serializers.TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

class TheaterFilms(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = serializers.TheaterSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            genres = Genre.objects.filter(**filter_dict)
            serialized_genres = GenreSerializer(genres, many=True)
            return Response(serialized_genres.data)
        else:
            return Response(GenreSerializer(Genre.objects.all(), many=True).data)

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            genres = Genre.objects.filter(**filter_dict)
            serialized_genres = GenreSerializer(genres, many=True)
            return Response(serialized_genres.data)
        else:
            return Response(GenreSerializer(Genre.objects.all(), many=True).data)
# Create your views here.
