from django.db import models

class Choco(models.Model):
    name = models.CharField(max_length=20)
    engridients = models.TextField(max_length=700)
    price = models.FloatField(default=1)
    
