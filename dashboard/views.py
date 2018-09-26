from django.shortcuts import render

from .utils import get_all_devices


def all_device_info(request):
    '''
    Obtain all the device information and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices()
    return render(request, 'dashboard.html', {'response': response})


def not_reported_for_two_days(request):
    pass
