from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class Post(models.Model):
    club = models.ForeignKey("squad.Squad", related_name="posts", on_delete=models.CASCADE)
    owner = models.ForeignKey("jwt_auth.User", related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=600)
    image = CloudinaryField("image", blank=True)

    def __str__(self):
        return f"Post by {self.owner.name} in club {self.club.name}"
