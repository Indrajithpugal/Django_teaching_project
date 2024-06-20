from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
