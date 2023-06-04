from django.contrib import admin
from .models import movies, series

# Register your models here.

class movieAdmin(admin.ModelAdmin):
    list_display = ['movie_id', 'movie_name', 'movie_des', 'movie_rating']


admin.site.register(movies, movieAdmin)


class seriesAdmin(admin.ModelAdmin):
    list_display = ['series_id', 'series_name', 'series_des', 'series_rating']


admin.site.register(series, seriesAdmin)