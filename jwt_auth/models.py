from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    debt = models.SmallIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
