from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .utils import get_account_info, return_device_info, return_all_imei


def account_device_info(request, account_key=None):
    api_key = get_account_info(account_key).api_key
    print(api_key)
    output = []
    imei_list = return_all_imei(account_key)
    for imei in imei_list:
        output.append(return_device_info(api_key, imei))
    return HttpResponse(output)
    # return render(request, 'account_device.html', {'output': output})


def account_contact(request, account_key):
    account_details = get_account_info(account_key)
    account_info = {
        'Name': account_details.account_name,
        'Address': account_details.account_address,
        'PhoneNumber': account_details.account_phone,
        'Comments': account_details.comments,
        'API_Key': account_details.api_key,
        'HOS_Key': account_details.hos_key,
    }
    return render(request, 'account_information.html', {'account_info': account_info})
