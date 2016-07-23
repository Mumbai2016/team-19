from rest_framework import serializers

from Api.models import EventRegistration


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = (
            'id',
            'member',
            'event',
            'created_at',
            'updated_at'
        )
