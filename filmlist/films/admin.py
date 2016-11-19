from django.contrib import admin

from .models import Film, Theater, Genre

# Register your models here.
admin.site.register(Film)
admin.site.register(Theater)
admin.site.register(Genre)
