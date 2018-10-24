from django.shortcuts import render

from .utils import get_all_devices_for_account


def not_reported_for_two_days(request, account_key):
    '''
    Obtain all the device information of the account and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices_for_account(account_key)
    return render(request, 'dashboard.html', {'response': response})
