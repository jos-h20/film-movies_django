from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    year_prod = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=150, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User',
        related_name='films',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ('title',)

class Theater(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=200, blank=True, default='')
    films = models.ManyToManyField(Film)

    owner = models.ForeignKey(
        'auth.User',
        related_name='theaters',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
