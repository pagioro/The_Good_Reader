from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    bio = models.CharField(max_length=254)
    known_for = models.CharField(max_length=254)
    image_url = models.CharField(max_length=254)