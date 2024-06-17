from django.db import models


# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=300)
    features = models.TextField(help_text="features of the mobile")
    and_version = models.IntegerField(default=0)
    rating = models.FloatField(default=3.4)
    launched = models.DateField(auto_now=True)
    offer = models.BooleanField(default=False)
    org_email = models.EmailField()
    website = models.URLField()
    mob_images = models.FileField(upload_to="mobile_images")
    price = models.BigIntegerField(default=10000)

    def __str__(self):
        return self.name

    @property
    def version_name(self):
        return f"{self.name},{self.and_version}"


class Accessories(models.Model):
    mobile_id = models.OneToOneField(Mobile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=30)

    def __str__(self):
        return self.item_name


class Review(models.Model):
    mobile_id = models.ForeignKey(Mobile, on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.mobile_id)


class Feedback(models.Model):
    mobile = models.ManyToManyField(Mobile)
    feedback_desc = models.TextField()

    def __str__(self):
        return self.feedback_desc
