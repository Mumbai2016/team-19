from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Api.models import Event, EventRegistration, Member
from Api.serializer.webapp.eventregistrationserializer import EventRegistrationSerializer
from Api.serializer.webapp.eventserializer import EventSerializer


@api_view(['POST'])
def event_create(request):
    event = request.data.get('event', None)
    ser = EventSerializer(data=event)
    if ser.is_valid():
        ser.save()

    else:
        return Response(data="Failed",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data="Success",status=status.HTTP_200_OK)


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


@api_view(['PUT'])
def event_register(request, eid, mid):
    try:
        er = EventRegistration.Objects.all()
    except EventRegistration.DoesNotExist:
        member = Member.Obejcts.get(pk=mid)
        event = Event.Obejcts.get(pk=eid)
        reg = {'event':event, 'member':member}
        ser = EventRegistrationSerializer(data=reg)
        if ser.is_valid():
            ser.save()
            return Response(data="Registered for Event", status=status.HTTP_200_OK)
        else:
            return Response(data="Failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)