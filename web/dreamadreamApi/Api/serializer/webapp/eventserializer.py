from rest_framework import serializers

from Api.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'description',
            'address',
            'qualification',
            'age_min',
            'age_max',
            'created_at',
            'updated_at'
        )
