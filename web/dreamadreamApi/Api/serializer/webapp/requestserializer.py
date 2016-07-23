from rest_framework import serializers

from Api.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = (
            'id',
            'member',
            'name',
            'description',
            'created_at',
            'updated_at'
        )
