from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre')
    exclude = ('date_created',)
    search_fields = ('title', 'genre__name')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
