from django.db import models

# Create your models here.


class Event(models.Model):
    club = models.ForeignKey("squad.Squad", related_name="events", on_delete=models.CASCADE)
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(decimal_places=2, max_digits=6)
    longitude = models.DecimalField(decimal_places=2, max_digits=6)
    total_cost = models.SmallIntegerField()
    total_players = models.SmallIntegerField()
    financier = models.ForeignKey(
        "jwt_auth.User", related_name="events", on_delete=models.CASCADE, default=None, blank=True, null=True
    )

    def __str__(self):
        return f"Event for {self.club} at {self.location} on {self.time}"
