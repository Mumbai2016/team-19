from rest_framework import serializers

from Api.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member

