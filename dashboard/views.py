import pprint

from django.shortcuts import render

from .utils import get_all_devices, get_all_parent_accounts, get_account_details, get_all_children_accounts


def show_all_accounts(request):
    parents_account_ID = get_all_parent_accounts()
    all_accounts = []
    for parent_key in parents_account_ID:
        try:
            all_accounts.append({
                'name': get_account_details(parent_key).account_name,
                'id': parent_key,
                'children': [get_account_details(child_key).account_name for child_key in
                             get_all_children_accounts(parent_key)]
            })
        except Exception as e:
            all_accounts.append({
                'name': get_account_details(parent_key).account_name,
                'id': parent_key,
                'children': ['No Account']
            })
            print(e)
    pprint.pprint(all_accounts)
    return render(request, 'accounts.html', {'all_accounts': all_accounts})


def not_reported_for_two_days(request):
    '''
    Obtain all the device information and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices()
    return render(request, 'dashboard.html', {'response': response})
