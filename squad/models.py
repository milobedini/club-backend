from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.

# NEED TO MAKE IMAGES OPTIONAL
class Squad(models.Model):
    name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    recurring = models.BooleanField(default=False)
    venue = models.CharField(max_length=100, default=None, blank=True)
    weekday = models.CharField(max_length=100, default=None, blank=True)
    image = CloudinaryField("image", default="")

    def __str__(self):
        return f"{self.name}"
