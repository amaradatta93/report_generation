import pprint

from django.http import HttpResponse
from django.shortcuts import render

from .utils import get_all_devices, convert_time_str_to_date_fromat


def all_device_info(request):
    '''
    Obtain all the device information and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices()
    return render(request, 'dashboard.html', {'response': response})


def not_reported_for_two_days(request):
    output = get_all_devices()
    pprint.pprint(output)
    response = []
    for device_info in output:
        for dates in device_info['Device']:
            date_str = dates['Last_Reported_Date']
            print(type(date_str))
            if date_str != 'Unknown':
                date_format = convert_time_str_to_date_fromat(date_str)
            print(type(date_format))
    return HttpResponse(output)
