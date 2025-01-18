from django.db import models

class Gourmet(models.Model):
    restaurant_name = models.CharField(max_length=50)
    memo = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(default=1)