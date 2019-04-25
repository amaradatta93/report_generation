from django.http import HttpResponseNotFound
from django.shortcuts import redirect


def days_html(request):
    request.session['temp_data'] = 2
    if request.GET.get('Account_Id'):
        request.session['Account_Id'] = request.GET.get('Account_Id')
        return redirect('/account/unresponsive/' + request.session['Account_Id'] + '/')
    else:
        return redirect('/dashboard')


def get_number_of_days(request):
    if request.method == 'POST':

        data_form = request.POST
        request.session['Account_Id'] = request.GET.get('Account_Id')

        if data_form['numberOfDays']:
            request.session['temp_data'] = data_form['numberOfDays']
        else:
            request.session['temp_data'] = 2

        if request.session['Account_Id']:
            print('not entering')
            return redirect('/account/unresponsive/' + request.GET.get('Account_Id') + '/')
        else:
            print('entering')
            return redirect('/dashboard/')
    else:
        return HttpResponseNotFound('Not found')
