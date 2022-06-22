from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    squads = models.ManyToManyField("squad.Squad", related_name="members", default=None, blank=True)
    admin_squads = models.ManyToManyField("squad.Squad", related_name="admin_members", blank=True)
    debt = models.SmallIntegerField(default=0)
    attending = models.ManyToManyField("events.Event", related_name="participants", default=None, blank=True)
    image = CloudinaryField("image", blank=True)

    def __str__(self):
        return f"{self.name}"
