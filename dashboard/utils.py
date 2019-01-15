from reports.utils import get_all_devices_for_account
from .models import *


def get_all_parent_accounts():
    '''
    get all accounts details
    :return: All accounts as an object
    '''
    parent_accounts = ParentAccount.objects.filter(parent_account_id=1)
    parent_id = [key.account_id for key in parent_accounts]
    return parent_id


def get_all_children_accounts(parent_key):
    children_accounts = ParentAccount.objects.filter(parent_account_id=parent_key)
    children_account_id = [key.account_id for key in children_accounts]
    return children_account_id


def get_all_devices(days):
    '''
    get all accounts, account id and the devices in the account
    :return: list of devices with the device information in it
    '''
    response = []
    all_accounts = Account.objects.all()
    for account in all_accounts:
        key = account.account_id
        account_devices = get_all_devices_for_account(key, days)
        for device in account_devices:
            response.append(device)

    return response
