from django.http import HttpResponse
from django.shortcuts import render

from .utils import get_all_devices, parse_time_threshold


def all_device_info(request):
    '''
    Obtain all the device information and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices()
    # return render(request, 'dashboard.html', {'response': response})
    return HttpResponse(response)


def not_reported_for_two_days(request):
    parsed_device_list = parse_time_threshold()
    # return HttpResponse(parsed_device_list)
    return render(request, 'dashboard.html', {'parsed_device_list': parsed_device_list})
