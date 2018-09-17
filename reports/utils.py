from .models import *


def get_account_info():
    account_details = Account()
    return account_details


def get_device_info(account_key):
    device_info = DeviceRegister.objects.filter(account_id=account_key)
    return device_info


def date_and_time(device_imei):
    device_info = DeviceDataView.objects.get(imei=device_imei)
    return [device_info.date_stamp, device_info.time_stamp]
