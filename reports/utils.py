from dashboard.utils import get_account_details, parsed_parameter


def get_all_devices_for_account(key):
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
            'account_devices': parsed_parameter(key)
        }
    )
    return response
