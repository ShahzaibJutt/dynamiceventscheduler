from rest_framework import serializers

from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'user', 'event']
        read_only_fields = ['user', 'event']

class RegistrationDetailSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source='event.title')

    class Meta:
        model = Registration
        fields = ('id', 'event_name')

