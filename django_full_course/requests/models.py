from django.db import models


# Create your models here.
class HousesDetails(models.Model):
    no_of_bedrooms = models.IntegerField()
    no_of_bathrooms = models.IntegerField()
    sqrt_feets = models.FloatField()
    price = models.IntegerField()
    desc = models.TextField()
