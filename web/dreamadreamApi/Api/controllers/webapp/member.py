import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import Member
from Api.serializer.webapp.memberserializer import MemberSerializer


@api_view(['GET'])
def list(request):
    members = Member.objects.all()
    retval = []
    for member in members:
        retval.append(MemberSerializer(member).data)
    return Response(data=retval, status=status.HTTP_200_OK)
