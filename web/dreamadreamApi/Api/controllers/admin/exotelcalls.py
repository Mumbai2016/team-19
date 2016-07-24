import datetime
import json

from rest_framework import status
from rest_framework.decorators import api_view

from Api.serializer.admin.ExotelResponseSerializer import ExotelResponseSerializer
from rest_framework.response import Response

from Api.utils.exotel import Exotel


@api_view(['POST'])
def make_exotel_call_task(request):
    data = request.data
    print(data)

    if 'mobile_nos[]' in data:

        exotel = Exotel()

        mobile_nos = request.POST.getlist('mobile_nos[]')

        unique_mobile_nos = set(mobile_nos)
        unique_mobile_nos = list(unique_mobile_nos)

        for mobile_no in unique_mobile_nos:
            resp = exotel.connect_number_to_app_without_callabck(to=mobile_no,
                                                                 app_id="103645",
                                                                 custom_field=mobile_no)
            resp = resp.json()
            print(resp)
            start_time = resp['Call']['DateCreated']
            data = {'callsid': resp['Call']['Sid'], 'start_time': start_time, 'mobile_no': mobile_no}
            print(data)
            ser = ExotelResponseSerializer(data=data)
            if ser.is_valid():
                ser.save()
                print(ser.data)
            else:
                print("Some Error occurred adding job data")

    return Response(data="Done", status=status.HTTP_200_OK)