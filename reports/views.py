from django.http import HttpResponse
from django.shortcuts import render, redirect


from .utils import get_all_devices_for_account


def not_reported_for_two_days(request, account_key):
    '''
    Obtain all the device information of the account and render it on the dashboard
    :param request:
    :return: list of devices as dictionary
    '''
    response = get_all_devices_for_account(account_key)
    return render(request, 'dashboard.html', {'response': response})


def get_not_reporting_time():
    pass


def days_html(request):
    return render(request, 'get_days.html', content_type='text/html')


def get_number_of_days(request):
    if request.method == 'POST':
        data_form = request.POST
        days = data_form['numberOfDays']
        return HttpResponse(days)
