import datetime

from reports.utils import get_all_account


def get_all_devices():
    '''
    get all accounts, account id and the devices in the account
    :return: list of devices with the device information in it
    '''
    pass
    # response = []
    # all_accounts = get_all_account()
    # for account in all_accounts:
    #     key = account.account_id
    #     response.append(return_device_info_with_date_time(key))
    # return response


def convert_time_str_to_date_fromat(date_str):
    date_format = datetime.datetime.strptime(date_str, '%d.%m.%Y')
    # two_days_back = datetime.date.today() - datetime.timedelta(days=2)
    # two_days_back = date_format - datetime.timedelta(days=2)
    # return two_days_back.strftime("%d.%m.%Y")
    return date_format
