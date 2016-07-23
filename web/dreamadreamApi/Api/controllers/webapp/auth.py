from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def register(request):
    user = request.data.get('user', None)
    return Response(data=user, status=status.HTTP_202_ACCEPTED)