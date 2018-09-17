from .models import *


def get_account_info():
    account_details = Account()
    return account_details


def get_device_info(account_key):
    device_info = DeviceRegister.objects.filter(account_id=account_key)
    return device_info

#
# def date_and_time(device_imei):
#     device_info = DeviceData.objects.filter(imei=device_imei)[:1]
#     for date_time in device_info:
#         return [date_time.date_stamp, date_time.time_stamp]
