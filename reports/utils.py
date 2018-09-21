from django.shortcuts import get_object_or_404

from .models import *


def get_all_account():
    '''
    Get all the accounts in the database
    :return: List of all the accounts
    '''
    all_accounts = Account.objects.all()
    return all_accounts


def get_account_name(account_key):
    '''
    Get the account name using the account_id
    :param account_key: The account_id linked to the account
    :return: The account_name corresponding to the account_id
    '''
    account_details = get_object_or_404(Account, account_id=account_key)
    return account_details.account_name


def return_device_dict(account_key):
    '''
    With the account_id extract the name associated with the account
    :param account_key: The account_id linked to the account
    :return: account_name, account_id and the empty device list as dictionary
    '''
    name = get_account_name(account_key)
    output = {
        'Account': name,
        'id': account_key,
        'Device': []
    }
    return output


def return_device_info(account_key):
    '''
    With the account_id extract the device health
    From return_device_dict() obtain the dictionary containing the name
    Append all the devices under that account into the empty device list
    Get the last reported date and time form date_and_time()
    :param account_key: The account_id linked to the account
    :return: name, id and the device list information as a dictionary
    '''
    device_info = DeviceRegister.objects.filter(account_id=account_key)
    device_details = return_device_dict(account_key)
    try:
        for device in device_info:
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
    except Exception as e:
        print(e)
        return return_device_dict(account_key)
    return device_details


def date_and_time(device_imei):
    '''
    Check the last reported date using the IMEI of the device
    If not found then returns unknown
    :param device_imei: The IMEI corresponding to the device
    :return: Last reported date and time as a list
    '''
    device_info = DeviceDataView.objects.filter(imei=device_imei)
    if device_info:
        for device_dt in device_info:
            return [device_dt.date_stamp, device_dt.time_stamp]
    else:
        return ['Unknown', 'Unknown']
