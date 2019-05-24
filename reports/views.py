from _datetime import datetime

from django.shortcuts import render

from .utils import get_all_devices_for_account


def not_reported_for_two_days(request, account_key):
    '''
    Obtain all the device information of the account and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    days = request.session['temp_data']
    response = get_all_devices_for_account(account_key, days)
    response[0]['account_devices'].sort(key=lambda x: datetime.strptime(x['last_reported_date'], '%d.%m.%Y'), reverse=True)
    return render(request, 'account_devices.html', {'response': response})

