from django.shortcuts import render

from .utils import return_device_info


def all_device_info(request, account_key=None):
    output = return_device_info(account_key)
    return render(request, 'dashboard.html', {'output': output})
