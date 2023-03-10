from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    bio = models.CharField(max_length=2056)
    known_for = models.CharField(max_length=254)
    image_url = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)