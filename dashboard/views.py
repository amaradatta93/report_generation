from django.shortcuts import render

from .utils import get_all_devices, get_all_parent_accounts, get_account_details, get_all_children_accounts


def show_all_accounts(request):
    '''
    Get all the parent and the child account and render it
    :param request:
    :return: list of dictionary containing the child account
    '''
    parents_account_id = get_all_parent_accounts()
    all_accounts = []
    for parent_key in parents_account_id:
        try:
            children_account_id = get_all_children_accounts(parent_key)
            children_account = []
            for child_id in children_account_id:
                try:
                    children_account.append(get_account_details(child_id))
                except Exception as e:
                    print(e)

            all_accounts.append({
                'name': get_account_details(parent_key).account_name,
                'id': parent_key,
                'children': children_account,
                'list_length': len(children_account) + 1,
            })

        except Exception as e:
            print(e)
    return render(request, 'accounts.html', {'all_accounts': all_accounts})


def not_reported_for_two_days(request):
    '''
    Obtain all the device information and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices()
    return render(request, 'dashboard.html', {'response': response})
