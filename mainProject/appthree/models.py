from django.db import models

# Create your models here.

class suggestInfo(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    description = models.TextField()
    type = models.CharField(max_length=20)


class contactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()