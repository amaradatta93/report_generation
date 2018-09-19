from django.shortcuts import render

from .utils import get_device_info, date_and_time, get_account_name


def all_device_info(request, account_key):
    device_info = get_device_info(account_key)
    name = get_account_name(account_key)
    output = {
        'Account': name,
        'Device': []
    }
    for device in device_info:
        date_time = date_and_time(device.imei)
        device_date = date_time[0]
        device_time = date_time[1]
        output['Device'].append({
            'IMEI': device.imei,
            'SIM_Number': device.sim_no,
            'Added_On': device.added_on,
            'Last_Reported_Date': device_date,
            'Last_Reported_Time': device_time,
            'Device_Status': device.device_status,
            'Billing_Status': device.billing_status,
            'Comments': device.comments.replace("\r\n", " "),
        })
    return render(request, 'dashboard.html', {'output': output})
