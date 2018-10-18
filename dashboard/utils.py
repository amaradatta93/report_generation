import pprint

from django.forms import model_to_dict

from reports.models import DeviceRegister, DeviceDataView
from reports.utils import get_all_account
from .parse_time_and_parameter import date_time_conversion, threshold_days_back


def get_all_devices():
    '''
    get all accounts, account id and the devices in the account
    :return: list of devices with the device information in it
    '''
    response = []
    all_accounts = get_all_account()
    for account in all_accounts:
        key = account.account_id
        response.append(
            {
                'account_name': account.account_name,
                'account_id': account.account_id,
                'account_devices': return_device_info_with_date_time(key)
            }
        )
        # response.update({'account_name': account.account_name})
        # response.update({'account_id': account.account_id})
        # response.update({'account_devices': return_device_info_with_date_time(key)})
    return response


def return_device_info_with_date_time(key):
    devices = []
    try:
        account_list = DeviceRegister.objects.filter(account_id=key)
        for account in account_list:
            device_info_list = DeviceRegister.objects.filter(imei=account.imei)

            for device_info in device_info_list:
                # try:
                date_time = DeviceDataView.objects.get(imei=device_info.imei)
                serialized_device_info = model_to_dict(device_info)
                serialized_device_info.update({'Last_Reported_Date': date_time.date_stamp})
                serialized_device_info.update({'Last_Reported_Time': date_time.time_stamp})
                devices.append(serialized_device_info)
                # except Exception as e:
                #     print(e)
                #     serialized_device_info['Last_Reported_Date'] = 'Unknown'
                #     serialized_device_info['Last_Reported_Time'] = 'Unknown'
                #     devices.append(serialized_device_info)

    except Exception as e:
        print(e)
    return devices


def parse_time_threshold():
    device_info = get_all_devices()
    parsed_device_list = []

    pprint.pprint(device_info)
    for devices in device_info:
        if device_info:
            # pprint.pprint(devices)
            for each_device in devices['account_devices']:
                try:
                    date_time_obj = date_time_conversion(each_device['Last_Reported_Date'],
                                                         each_device['Last_Reported_Time'])
                    print('loop2')
                    dt_check = threshold_days_back(date_time_obj, 10)
                    if dt_check and ((each_device['device_status'] == 'Active') and (each_device['billing_status'] == 'Active')):
                        # print(devices['Last_reported_date'], devices['Last_reported_time'], devices['Device_Status'], devices['Billing_Status'])
                        parsed_device_list.append(devices)
                except KeyError:
                    devices.update({'Last_Reported_Date': 'not found'})
                    devices.update({'Last_Reported_Time': 'not found'})
                    parsed_device_list.append(devices)
    # pprint.pprint(parsed_device_list)
    return parsed_device_list
