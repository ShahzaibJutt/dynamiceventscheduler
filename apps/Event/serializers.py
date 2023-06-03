from rest_framework import serializers

from apps.Event.models import Event


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Event
        fields = ["title", "event_location", "date", "description", "image_url", "id"]
