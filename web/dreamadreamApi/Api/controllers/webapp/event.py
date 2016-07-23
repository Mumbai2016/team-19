from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import Event
from Api.serializer.webapp.eventserializer import EventSerializer


@api_view(['POST'])
def createEvent(request):
    event = request.data.get('event', None)
    #   Create Event
    ser = EventSerializer(data=event)
    if ser.is_valid():
        ser.save()
    else:
        return None

    return event


# @api_view(['GET'],['PUT'])
# def details(request, eid):
