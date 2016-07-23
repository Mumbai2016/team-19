from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.controllers.webapp.auth import register
from Api.models import Member
from Api.serializer.webapp.memberserializer import MemberSerializer


@api_view(['GET'])
def member_detail(request, id):
    try:
        member = Member.objects.get(pk=id)
    except Member.DoesNotExist:
        return Response(data="Member not found", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        member = MemberSerializer(member).data
        return Response(data=member, status=status.HTTP_200_OK)


@api_view(['POST'])
def member_create(request):
    register(request)


@api_view(['GET'])
def member_delete(request, id):
    try:
        member = Member.objects.get(pk=id)
    except:
        return Response(data="Member not found", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        member.is_deactivated = True
        member.save()
        return Response(data="Member deleted", status=status.HTTP_200_OK)