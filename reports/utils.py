from .models import *


def get_account_name(account_key):
    account_details = Account.objects.get(account_id=account_key)
    return account_details.account_name


def get_device_info(account_key):
    device_info = DeviceRegister.objects.filter(account_id=account_key)
    return device_info


def date_and_time(device_imei):
    device_info = DeviceDataView.objects.get(imei=device_imei)
    return [device_info.date_stamp, device_info.time_stamp]
