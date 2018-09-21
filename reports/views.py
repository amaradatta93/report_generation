from django.shortcuts import render

from .utils import return_device_info


def account_device_info(request, account_key=None):
    '''
    Get all the devices under a particular account
    :param request:
    :param account_key: The account_id linked to the account
    :return: Device information of that particular account, as dictionary
    '''
    output = return_device_info(account_key)
    return render(request, 'account_device.html', {'output': output})
