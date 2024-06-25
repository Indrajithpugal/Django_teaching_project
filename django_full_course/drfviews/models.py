from django.db import models

# Create your models here.


class Groceries(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    rating = models.FloatField()
    review = models.TextField()

    def __str__(self):
        return self.name


class Images(models.Model):
    grocery_image = models.FileField(upload_to="grocery_images")
    grocery_id = models.ForeignKey(Groceries, on_delete=models.CASCADE)
