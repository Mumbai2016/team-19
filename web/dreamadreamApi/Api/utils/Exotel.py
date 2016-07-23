import requests
from django.conf import settings


class Exotel:

    def __init__(self):
        self._config = ExotelConfig()
        self.automated_apply_call_app_id = self._config.automated_apply_call_app_id
        self.automated_interview_call_app_id = self._config.automated_interview_call_app_id
        self.automated_interview_dna_call_app_id = self._config.automated_interview_dna_call_app_id

    def connect_number_to_app(self, to, app_id, custom_field, callback_url,
                              time_limit=None, timeout=None, caller_id=None, call_type="trans"):

        if caller_id is None:
            caller_id = self._config.caller_id_1
        sid = self._config.sid
        token = self._config.token
        app_url = "http://my.exotel.in/exoml/start/{app_id}".format(app_id=app_id)
        url = "https://{sid}:{token}@twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json".format(sid=sid, token=token)
        data = {
            'From': to,
            'CallerId': caller_id,
            'CallType': call_type,
            'Url': app_url,
            'TimeLimit': time_limit,
            'TimeOut': timeout,
            'StatusCallback': callback_url,
            'CustomField': custom_field
        }
        return requests.post(url, data)

    def connect_number_to_app_without_callabck(self, to, app_id, custom_field,
                              time_limit=None, timeout=None, caller_id=None, call_type="trans"):

        if caller_id is None:
            caller_id = self._config.caller_id_1
        sid = self._config.sid
        token = self._config.token
        app_url = "http://my.exotel.in/exoml/start/{app_id}".format(app_id=app_id)
        url = "https://{sid}:{token}@twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json".format(sid=sid, token=token)
        data = {
            'From': to,
            'CallerId': caller_id,
            'CallType': call_type,
            'Url': app_url,
            'TimeLimit': time_limit,
            'TimeOut': timeout,
            'CustomField': custom_field
        }
        return requests.post(url, data)

    def get_call_status(self, call_sid):
        sid = self._config.sid
        token = self._config.token
        url = "https://{sid}:{token}@twilix.exotel.in/v1/Accounts/{sid}/Calls/{call_sid}.json".format(sid=sid, token=token, call_sid=call_sid)

        return requests.get(url=url)

class ExotelConfig:
    def __init__(self):
        self.sid = settings.EXOTEL['sid']
        self.token = settings.EXOTEL['token']
        self.caller_id_1 = settings.EXOTEL['caller_id_1']
        self.caller_id_2 = settings.EXOTEL['caller_id_2']
        self.outgoing_call_app_id = settings.EXOTEL['outgoing_call_app_id']
