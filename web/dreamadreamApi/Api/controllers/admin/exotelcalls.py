import datetime

from Api.serializer.admin.ExotelResponseSerializer import ExotelResponseSerializer
from dreamadreamApi.settings import EXOTEL


def make_exotel_call_task(request):
    data = request.data;

    if 'mobile_nos' in data:

        exotel = EXOTEL()

        mobile_nos = data['mobile_nos']

        unique_mobile_nos = set(mobile_nos)
        unique_mobile_nos = list(unique_mobile_nos)

        for mobile_no in unique_mobile_nos:
            try:
                resp = exotel.connect_number_to_app_without_callabck(to=mobile_no,
                                                                     app_id=exotel.automated_interview_dna_call_app_id,
                                                                     custom_field=mobile_no)
                resp = resp.json()
                start_time = resp['Call']['DateCreated']
                start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                data = {'callsid': resp['Call']['Sid'], 'start_time': start_time, 'mobile_no': mobile_no}
                ser = ExotelResponseSerializer(data=data)
                if ser.is_valid():
                    ser.save()
                else:
                    print("Some Error occurred adding job data")
            except:
                print("Call failed for "+ mobile_no)