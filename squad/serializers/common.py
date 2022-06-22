from rest_framework import serializers

from ..models import Squad


class SquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squad
        fields = ("id", "name", "sport", "recurring", "venue", "weekday", "members", "admin_members")
