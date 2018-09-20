from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import *


def get_all_account():
    all_accounts = Account.objects.all()
    return all_accounts


def get_account_name(account_key):
    account_details = get_object_or_404(Account, account_id=account_key)
    return account_details.account_name


def return_device_dict(account_key):
    name = get_account_name(account_key)
    output = {
        'Account': name,
        'id': account_key,
        'Device': []
    }
    return output


def return_device_info(account_key):
    device_info = DeviceRegister.objects.filter(account_id=account_key)
    device_details = return_device_dict(account_key)
    if device_info:
        for device in device_info:
            print('test2')
            date_time = date_and_time(device.imei)
            device_date = date_time[0]
            device_time = date_time[1]
            device_details['Device'].append({
                'IMEI': device.imei,
                'SIM_Number': device.sim_no,
                'Added_On': device.added_on,
                'Last_Reported_Date': device_date,
                'Last_Reported_Time': device_time,
                'Device_Status': device.device_status,
                'Billing_Status': device.billing_status,
                'Comments': device.comments.replace("\r\n", " "),
            })
    print(device_details)
    return device_details


def date_and_time(device_imei):
    device_info = get_object_or_404(DeviceDataView, imei=device_imei)
    return [device_info.date_stamp, device_info.time_stamp]
