import pprint

from django.forms import model_to_dict

from .models import DeviceRegister, DeviceDataView, Account, ParentAccount
from .parse_time_and_parameter import date_time_conversion, threshold_days_back


def get_account_details(key):
    '''
    Get a specific account using the id associated with it
    :param key: Account Id associated with the corresponding account
    :return: The account object
    '''
    account = Account.objects.get(account_id=key)
    return account


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


def get_all_devices():
    '''
    get all accounts, account id and the devices in the account
    :return: list of devices with the device information in it
    '''
    response = []
    all_accounts = Account.objects.all()
    for account in all_accounts:
        key = account.account_id
        response.append(
            {
                'account_name': account.account_name,
                'account_id': account.account_id,
                'account_devices': parsed_parameter(key)
            }
        )
    pprint.pprint(response)
    return response


def return_device_info_with_date_time(key):
    '''
    For all the device include a field indicating the last reported date
    and time of the devices
    :param key: Account Id associated with the corresponding account
    :return:
    '''
    devices = []
    try:
        account_list = DeviceRegister.objects.filter(account_id=key)
        for account in account_list:
            device_info_list = DeviceRegister.objects.filter(imei=account.imei)

            for device_info in device_info_list:
                date_time = DeviceDataView.objects.get(imei=device_info.imei)
                serialized_device_info = model_to_dict(device_info)
                serialized_device_info.update({'Last_Reported_Date': date_time.date_stamp})
                serialized_device_info.update({'Last_Reported_Time': date_time.time_stamp})
                devices.append(serialized_device_info)
    except Exception as e:
        print(e)
    return devices


def parse_time_threshold(key):
    '''
    Filter out the device which have device and billing status as Active and which have not
    been reporting for set number of days
    :param key: Account Id associated with the corresponding account
    :return: List of device as dictionary which qualify the above criteria
    '''
    devices_list = return_device_info_with_date_time(key)
    parsed_device_list = []

    for each_device in devices_list:
        try:
            date_time_obj = date_time_conversion(each_device['Last_Reported_Date'],
                                                 each_device['Last_Reported_Time'])
            dt_check = threshold_days_back(date_time_obj, 7)
            if dt_check and (
                    (each_device['device_status'] == 'Active') and (each_device['billing_status'] == 'Active')):
                parsed_device_list.append(each_device)
        except KeyError:
            each_device.update({'Last_Reported_Date': 'not found'})
            each_device.update({'Last_Reported_Time': 'not found'})
            parsed_device_list.append(each_device)
    return parsed_device_list


def parsed_parameter(key):
    '''
    Filter out all the unnecessary dictionary parameters
    :param key: Account Id associated with the corresponding account
    :return:List of device as dictionary with desired parameters
    '''
    parsed_device_list = parse_time_threshold(key)

    parsed_parameter_list = []
    for each_device in parsed_device_list:
        parsed_parameter_list.append(
            {
                'imei': each_device['imei'],
                'sim_number': each_device['sim_no'],
                'added_on': each_device['added_on'],
                'last_reported_date': each_device['Last_Reported_Date'],
                'last_reported_time': each_device['Last_Reported_Time'],
            }
        )
    return parsed_parameter_list
