import pprint

from django.shortcuts import render

from .utils import return_device_info, get_all_account, return_device_dict


def all_device_info(request, account_key=None):
    if account_key is None:
        response = []
        all_accounts = get_all_account()
        for account in all_accounts:
            key = account.account_id
            response.append(return_device_info(key))
        return render(request, 'dashboard.html', {'response': response})
    else:
        output = return_device_info(account_key)
        print(type(output))
        # pprint.pprint(output)
        return render(request, 'account_device.html', {'output': output})
