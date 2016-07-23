import json

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
        Member.objects.get(email_id=user.email_id)
        User.objects.get(username=user.email_id)
    except (Member.DoesNotExist, User.DoesNotExist):
        return Response(data="User Already exists please try again")
    else:
        user = _register(request=request)

    return Response(data=user, status=status.HTTP_202_ACCEPTED)


def login(request):
    user = request.data.get('user', None)
    try:
        Member.objects.get(email_id=user.email_id)
        User.objects.get(username=user.email_id)
    except (Member.DoesNotExist, User.DoesNotExist):
        return Response(data="User Not registered")
    else:
        user = authenticate(username=user.email_id, password=user.password)
        return Response(data=user)


def _register(request):
    user = User.objects.create_user(
        username=request.data['user']['email_id'], password=request.data['user']['password'])
    #   Create Member
    member = json.dumps(request.data['user'])
    ser = MemberSerializer(data=member)
    if ser.is_valid():
        ser.save()
    else:
        return None

    return user
