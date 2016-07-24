import json
from datetime import datetime

import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import Member
from Api.serializer.webapp.memberserializer import MemberSerializer


@api_view(['POST'])
def register(request):
    user = request.data.get('user', None)

    try:
        Member.objects.get(email_id=user['email_id'])
    except Member.DoesNotExist:
        user, member = _register(request=request)
        retval = {
            'user': user.username,
            'member': member.id
        }
        return Response(data=retval, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(data="User Already exists please try again")


@api_view(['POST'])
def login(request):
    user = request.data.get('user', None)

    try:
        member = Member.objects.get(email_id=user['email_id'])
    except Member.DoesNotExist:
        return Response(data="User Not registered")
    else:
        user = authenticate(username=user['email_id'], password=user['password'])
        retval = {
            'user': user.username,
            'member': member.id
        }
        return Response(data=retval, status=status.HTTP_202_ACCEPTED)


def _register(request):
    user = User.objects.create_user(
        username=request.data['user']['email_id'],
        password=request.data['user']['password'])
    #   Create Member
    member = request.data['user']
    ser = MemberSerializer(data=member)
    if ser.is_valid():
        member = ser.save()
    else:
        raise ValueError(json.dumps(ser.errors))

    return user, member
