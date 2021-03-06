from rest_framework import serializers

from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "club",
            "time",
            "location",
            "longitude",
            "latitude",
            "total_cost",
            "total_players",
            "participants",
            "financier",
        )
