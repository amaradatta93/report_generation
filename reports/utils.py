from django.forms import model_to_dict

from dashboard.models import Account, DeviceType, DeviceRegister, DeviceDataView
from dashboard.parse_time_and_parameter import date_time_conversion, threshold_days_back


def get_all_devices_for_account(key, days):
    '''
    get all accounts, account id and the devices in the account
    :param key: Account Id associated with the corresponding account
    :return: list of devices with the device information in it
    '''
    response = []
    account = get_account_details(key)
    key = account.account_id
    response.append(
        {
            'account_name': account.account_name,
            'account_id': account.account_id,
            'account_devices': parsed_parameter(key, days)
        }
    )
    return response


def get_account_details(key):
    '''
    Get a specific account using the id associated with it
    :param key: Account Id associated with the corresponding account
    :return: The account object
    '''
    account = Account.objects.get(account_id=key)
    return account


def parsed_parameter(key, days):
    '''
    Filter out all the unnecessary dictionary parameters
    :param key: Account Id associated with the corresponding account
    :return:List of device as dictionary with desired parameters
    '''

    parsed_device_list = parse_time_threshold(key, days)
    parsed_parameter_list = []

    for each_device in parsed_device_list:
        parsed_parameter_list.append(
            {
                'device_name': get_device_name(each_device['device_type_id']),
                'imei': each_device['imei'],
                'sim_number': each_device['sim_no'],
                'added_on': each_device['added_on'],
                'last_reported_date': each_device['Last_Reported_Date'],
                'last_reported_time': each_device['Last_Reported_Time'],
            }
        )
    return parsed_parameter_list


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
                try:
                    date_time = DeviceDataView.objects.get(imei=device_info.imei)
                    serialized_device_info = model_to_dict(device_info)
                    serialized_device_info.update({'Last_Reported_Date': date_time.date_stamp})
                    serialized_device_info.update({'Last_Reported_Time': date_time.time_stamp})
                    devices.append(serialized_device_info)
                except Exception as e:
                    print(e)

    except Exception as e:
        print(e)

    return devices


def parse_time_threshold(key, days_threshold):
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
            dt_check = threshold_days_back(date_time_obj, days_threshold)
            if dt_check and (
                    (each_device['device_status'] == 'Active') and (each_device['billing_status'] == 'Active')):
                parsed_device_list.append(each_device)
        except KeyError:
            each_device.update({'Last_Reported_Date': 'not found'})
            each_device.update({'Last_Reported_Time': 'not found'})
            parsed_device_list.append(each_device)
    return parsed_device_list


def get_device_name(id):
    device_name = DeviceType.objects.get(device_type_id=id)
    return device_name.device_type
