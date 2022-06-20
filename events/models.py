from django.db import models

# Create your models here.


class Event(models.Model):
    club = models.ForeignKey("squad.Squad", related_name="events", on_delete=models.CASCADE)
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    total_cost = models.SmallIntegerField()
    # participants =
    # financier =

    def __str__(self):
        return f"Event for {self.club} at {self.location} on {self.time}"
