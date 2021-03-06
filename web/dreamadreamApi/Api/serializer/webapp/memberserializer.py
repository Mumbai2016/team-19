from rest_framework import serializers

from Api.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'full_name',
            'email_id',
            'password',
            'address',
            'gender',
            'dob',
            'age',
            'mobile_no',
            'mother_mobile_no',
            'father_mobile_no',
            'other_no',
            'goal',
            'reward_points',
            'program_start_date',
            'program_duration',
            'is_active',
            'is_approved',
            'is_deactivated',
            'deactivated_on',
            'created_at',
            'updated_at'
        )
