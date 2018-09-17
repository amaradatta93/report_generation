from django.http import JsonResponse

from .utils import get_device_info, date_and_time


def all_device_info(request, account_key):
    device_info = get_device_info(account_key)
    output = []
    for device in device_info:
        date_time = date_and_time(device.imei)
        device_date = date_time[0]
        device_time = date_time[1]
        output.append({
            'IMEI': device.imei,
            'SIM Number': device.sim_no,
            'Added On': device.added_on,
            'Last Reported Date': device_date,
            'Last Reported Time': device_time,
            'Device Status': device.device_status,
            'Billing Status': device.billing_status,
            'Comments': device.comments.replace("\r\n", " "),
        })
    return JsonResponse({'Account_Id': account_key, 'Device': output})
