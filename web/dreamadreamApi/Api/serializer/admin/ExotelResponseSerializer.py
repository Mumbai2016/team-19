from rest_framework import serializers

from Api.models import Call


class ExotelResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Call
        fields = (
            'id',
            'callsid',
            'mobile_no',
            'response',
            'start_time',
            'end_time',
            'duration',
            'created_at',
            'updated_at'
        )

    # def create(self, validated_data):
    #     exotelResoponse = Call.objects.create(**validated_data)
    #     return exotelResoponse
