from django.shortcuts import render

from get_days.views import pass_days
from .utils import get_all_devices_for_account


def not_reported_for_two_days(request, account_key):
    '''
    Obtain all the device information of the account and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    days = pass_days()
    print('i think the mistake is here {}'.format(days))
    response = get_all_devices_for_account(account_key, days)
    return render(request, 'dashboard.html', {'response': response})
