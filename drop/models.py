from django.db import models
class Items(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
