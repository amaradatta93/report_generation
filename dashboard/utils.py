from reports.utils import get_all_account, return_device_info


def get_all_devices():
    '''
    get all accounts, account id and the devices in the account
    :return: list of devices with the device information in it
    '''
    response = []
    all_accounts = get_all_account()
    for account in all_accounts:
        key = account.account_id
        response.append(return_device_info(key))
    return response
