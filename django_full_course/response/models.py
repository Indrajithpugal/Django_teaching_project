from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=900)
    rating = models.FloatField()

    def __str__(self):
        return self.name
