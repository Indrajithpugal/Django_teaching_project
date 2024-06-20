from django.db import models


# Create your models here.
class Laptop(models.Model):
    brand = models.CharField(max_length=40)
    os_type = models.CharField(max_length=40)
    size = models.FloatField(default=14)
    color = models.CharField(max_length=40)
    price = models.IntegerField()

    def __str__(self):
        return self.brand
