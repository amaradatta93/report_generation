import pprint

from django.shortcuts import render

from .utils import return_device_info, get_all_account, return_device_dict


def all_device_info(request, account_key=None):
    if account_key is None:
        aai = []
        all_accounts = get_all_account()
        for account in all_accounts:
            # print(account.account_id)
            key = account.account_id
            response = return_device_dict(key)
            aai.append(response)
            # pprint.pprint(aai)
        pprint.pprint(aai)
        return render(request, 'dashboard.html', {'aai': aai})
    else:
        output = return_device_info(account_key)
        print(type(output))
        # pprint.pprint(output)
    return render(request, 'account_device.html', {'output': output})
