import pprint

from django.shortcuts import render

from .utils import get_all_devices, get_all_parent_accounts, get_account_details, get_all_children_accounts


def show_all_accounts(request):
    parents_account_id = get_all_parent_accounts()
    all_accounts = []
    for parent_key in parents_account_id:
        parent_name = get_account_details(parent_key).account_name
        try:
            children_account = [get_account_details(child_key).account_name for child_key in
                                get_all_children_accounts(parent_key)]
            all_accounts.append({
                'name': parent_name,
                'toggle_id': parent_name.replace(" ", "-"),
                'id': parent_key,
                'children': children_account,
                'list_length': len(children_account) + 1,
            })
        except Exception as e:
            all_accounts.append({
                'name': parent_name,
                'toggle_id': parent_name.replace(" ", "-"),
                'id': parent_key,
                'children': None
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
