from rest_framework import serializers

from Api.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'member',
            'event',
            'feedback',
            'created_at',
            'updated_at'
        )
