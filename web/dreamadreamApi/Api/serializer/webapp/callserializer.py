from rest_framework import serializers

from Api.models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = (
            'id',
            'member',
            'call_date',
            'status_at_date',
            'created_at',
            'updated_at'
        )
