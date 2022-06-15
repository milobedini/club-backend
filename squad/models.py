from django.db import models

# Create your models here.


class Squad(models.Model):
    name = models.CharField(max_length=100)
    # members
    # admin members
    sport = models.CharField(max_length=100)
    recurring = models.BooleanField(default=False)
    venue = models.CharField(max_length=100, default=None)
    weekday = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f"{self.name}"