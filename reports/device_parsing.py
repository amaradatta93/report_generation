import pprint
from urllib.parse import urlencode
import xml.etree.ElementTree as ET
import requests

from .models import DeviceDataView


def return_response(api_key, imei):
    params = urlencode(dict(KEY=api_key, IMEI=imei))
    url = 'https://us01.infotrak.us/KlikoAPI/xml_last_known_loc_imei?{0}'.format(params)
    response = requests.get(url)
    return response


def parse_response(api_key, imei):
    response = return_response(api_key, imei)
    root = ET.fromstring(response.content)
    device_info = {}

    for child in root:
        device_info[child.tag] = child.text
    return device_info





































def date_and_time(device_imei):
    '''
    Check the last reported date using the IMEI of the device
    If not found then returns unknown
    :param device_imei: The IMEI corresponding to the device
    :return: Last reported date and time in a list.
             If both are not found 'Unknown' is returned
    '''
    device_info = DeviceDataView.objects.filter(imei=device_imei)
    if device_info:
        for device_dt in device_info:
            return [device_dt.date_stamp, device_dt.time_stamp]
    else:
        return ['Unknown', 'Unknown']
