from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
