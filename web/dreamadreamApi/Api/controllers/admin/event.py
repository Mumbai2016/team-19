from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import Event
from Api.serializer.webapp.eventserializer import EventSerializer


@api_view(['POST'])
def create_event(request):
    event = request.data.get('event', None)
    ser = EventSerializer(data=event)
    if ser.is_valid():
        ser.save()
    else:
        return None

    return event


@api_view(['GET'])
def event_list(request):
    events = Event.Objects.all()
    retval = []
    for event in events:
        retval.append(EventSerializer(event).data)
    return Response(data=retval, status=status.HTTP_200_OK)


@api_view(['GET'])
def event_delete(request, id):
    try:
        event = Event.objects.get(pk=id)
    except:
        return Response(data="Event not found", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        event.is_disabled = True
        event.save()
        return Response(data="Event deleted", status=status.HTTP_200_OK)