"""filmlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from films import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^films$', views.film_list, name='films'),
    url(r'^api/films$', views.api_film_list),
    url(r'^films/(?P<pk>[0-9]+)$', views.film_detail, name='film'),
    url(r'^api/films/(?P<pk>[0-9]+)$', views.api_film_detail),
    url(r'^theaters$', views.theater_list, name='theaters'),
    url(r'^api/theaters$', views.api_theater_list),
    url(r'^theaters/(?P<pk>[0-9]+)$', views.theater_detail, name='theater'),
    url(r'^api/theaters/(?P<pk>[0-9]+)$', views.api_theater_detail),
    # url(r'^theater_films/(?P<pk>[0-9]+)$', views.theater_films),
    url(r'^api/theater_films/(?P<pk>[0-9]+)$', views.api_theater_films),
    url(r'^genres$', views.genre_list, name='genres'),
    url(r'^api/genres$', views.api_genre_list),
    url(r'^genres/(?P<pk>[0-9]+)$', views.genre_detail, name='genre'),
    url(r'^api/genres/(?P<pk>[0-9]+)$', views.api_genre_detail),
    url(r'^post_url$', views.post_film, name='post_film'),
    # url(r'^$', views.ListCreateFilm.as_view(), namespace='films'),
    # url(r'(?P<pk>\d+)$',
    #     views.RetrieveUpdateDestroyFilm.as_view(),
    #     namespace='films'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
