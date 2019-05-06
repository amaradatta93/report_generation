import csv
import datetime
import json

import pytz
from django.http import HttpResponse
from django.shortcuts import render

from reports.utils import get_account_details
from .utils import get_all_devices, get_all_parent_accounts, get_all_children_accounts


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

    days = request.session['temp_data']
    response = get_all_devices(days)
    return render(request, 'dashboard.html', {'response': response})


def write_csv(request):
    '''
    Get the response from the dashboard and then convert the response into a csv file
    and download it onto the local system
    :param request:
    :return: download the file to local system
    '''
    response = None
    if request.method == 'POST':
        response = dict(request.POST)
        request_response = json.loads(response['downloadAsCsv'][0].replace("'", '"'))
        threshold_days = request.session['temp_data']

        csv_columns = ['account_name', 'device_name', 'imei', 'sim_number', 'last_reported_date', 'last_reported_time',
                       'added_on']
        csv_name = 'Unresponsive_device_' + str(datetime.datetime.now(pytz.timezone('US/Pacific')).date()) + '.csv'
        print('The unresponsive device report is available in "{0}"'.format(csv_name))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="' + csv_name + '"'

        try:
            description_text = 'Device which have not reported since or before last ' + str(threshold_days) + ' days'
            description = csv.writer(response)
            description.writerow([description_text])
            writer = csv.DictWriter(response, dialect='excel', fieldnames=csv_columns)
            writer.writeheader()

            for each_account_devices in request_response:
                device_list = each_account_devices['account_devices']

                if device_list:
                    for each_device in device_list:
                        each_device['account_name'] = each_account_devices['account_name']
                        writer.writerow(each_device)
        except IOError:
            print("I/O error")

    return response
