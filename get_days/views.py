from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse


def days_html(request, Account_Id=None):
    request.session['temp_data'] = 2
    request.session['Account_Id'] = request.GET.get('Account_Id')
    print('---------------------------------------------------')
    print(request.GET.get('Account_Id'))

    if request.GET.get('Account_Id') == 'None':
        return redirect(reverse('dashboard:account_name'))
    else:
        request.session['Account_Id'] = request.GET.get('Account_Id')
        return redirect('../../account/unresponsive/' + request.session['Account_Id'] + '/')


def get_number_of_days(request, Account_Id=None):

    if request.method == 'POST':

        data_form = request.POST

        if data_form['numberOfDays']:
            request.session['temp_data'] = data_form['numberOfDays']
        else:
            request.session['temp_data'] = 2

        if request.session['Account_Id'] != 'None':
            return redirect('../account/unresponsive/' + request.session['Account_Id'] + '/')
        else:
            return redirect(reverse('dashboard:account_name'))
    else:
        return HttpResponseNotFound('Not found')
