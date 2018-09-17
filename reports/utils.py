from .models import *


def get_account_info():
    account_details = Account()
    return account_details


def get_device_info(account_id):
    if account_id is None:
        device_info = DeviceRegister.objects.all()
    else:
        device_info = DeviceRegister.objects.filter(Account_ID=account_id)
    return device_info
