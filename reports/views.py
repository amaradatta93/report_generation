from django.shortcuts import render

from .utils import get_account_info, return_device_info_with_date_time


def account_device_info(request, account_key=None):
    '''
    Get all the devices under a particular account
    :param request:
    :param account_key: The account_id linked to the account
    :return: Device information of that particular account, as dictionary
    '''
    output = return_device_info_with_date_time(account_key)
    return render(request, 'account_device.html', {'output': output})


def account_contact(request, account_key):
    account_info = get_account_info(account_key)
    return render(request, 'account_information.html', {'account_info': account_info})
