from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "club", "owner", "created_at", "text", "image")
