from django.http import JsonResponse

from .utils import get_device_info, date_and_time


def all_device_info(request, account_key):
    device_info = get_device_info(account_key)
    output = []
    for device in device_info:
        # date_time = date_and_time(device.imei)
        # # print(date_time)
        # device_date = date_time[0]
        # device_time = date_time[1]
        output.append({
            'IMEI': device.imei,

        })
    return JsonResponse({'Account_Id': account_key, 'Device': output})
