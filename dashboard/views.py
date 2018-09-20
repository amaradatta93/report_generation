from django.shortcuts import render

from reports.utils import get_all_account, return_device_info


def all_device_info(request):
    response = []
    all_accounts = get_all_account()
    for account in all_accounts:
        key = account.account_id
        response.append(return_device_info(key))
    return render(request, 'dashboard.html', {'response': response})
