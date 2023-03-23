from django.db import models

class Bugreport(models.Model):
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    browser = models.CharField(max_length=254)
    os = models.CharField(max_length=254)
    resolution = models.CharField(max_length=254)
