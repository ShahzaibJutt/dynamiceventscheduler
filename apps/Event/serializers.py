from rest_framework import serializers

from apps.Event.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["title", "event_location", "date", "description"]
