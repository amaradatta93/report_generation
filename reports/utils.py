from .models import *


def get_account_name_id(account_key):
    account_details = Account.objects.get(account_id=account_key)
    return account_details.account_name, account_details.account_id


def get_device_info(account_key):
    device_info = DeviceRegister.objects.filter(account_id=account_key)
    return device_info


def return_device_info(account_key):
    device_info = get_device_info(account_key)
    name, key = get_account_name_id(account_key)
    output = {
        'Account': name,
        'id': key,
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
    return output


def date_and_time(device_imei):
    device_info = DeviceDataView.objects.get(imei=device_imei)
    return [device_info.date_stamp, device_info.time_stamp]
