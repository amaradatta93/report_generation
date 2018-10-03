from django.shortcuts import get_object_or_404, get_list_or_404

from .device_parsing import parse_response
from .models import *


def get_all_account():
    '''
    Get all the accounts in the database
    :return: List of all the accounts
    '''
    all_accounts = Account.objects.all()
    return all_accounts


def get_account_info(account_key):
    '''
    Get the account details using the account_id
    :param account_key: The account_id linked to the account
    :return: Complete account details as an object
    '''
    account_details = get_object_or_404(Account, account_id=account_key)
    return account_details


def return_all_imei(account_key):
    account = get_list_or_404(DeviceRegister, account_id=account_key)
    imei = [each_device.imei for each_device in account]
    return imei


def return_device_info(api_key, imei):
    response = parse_response(api_key, imei)
    comment_billing = get_comment_and_billing_status(imei)
    response['billing_status'] = comment_billing['billing_status']
    response['comments'] = comment_billing['comments']
    return response


def get_comment_and_billing_status(IMEI):
    comment_billing = {}
    try:
        comment_billing_info = get_object_or_404(DeviceRegister, imei=IMEI)
        comment_billing['billing_status'] = comment_billing_info.billing_status
        comment_billing['comments'] = comment_billing_info.comments
    except Exception as e:
        print(e)
        comment_billing['billing_status'] = None
        comment_billing['comments'] = None
    return comment_billing
