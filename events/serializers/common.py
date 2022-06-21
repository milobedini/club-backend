from rest_framework import serializers

from ..models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "club",
            "time",
            "location",
            "total_cost",
            "participants",
        )
