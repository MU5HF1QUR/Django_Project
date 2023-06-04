from django.db import models

# Create your models here.

class movies(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=100)
    movie_des = models.TextField()
    movie_rating = models.FloatField()


class series(models.Model):
    series_id = models.IntegerField()
    series_name = models.CharField(max_length=100)
    series_des = models.TextField()
    series_rating = models.FloatField()
    

