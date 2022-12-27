from django.db import models

class Wishlist(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    added_date = models.IntegerField()