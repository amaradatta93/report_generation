from django.shortcuts import render, redirect
import pprint

def days_html(request):
    pprint.pprint(request.GET.get('Account_Id'))
    request.session['Account_Id'] = request.GET.get('Account_Id')
    return render(request, 'get_days.html', content_type='text/html')


def get_number_of_days(request):
    pprint.pprint(request.session.keys())

    if request.method == 'POST':
        data_form = request.POST
        request.session['temp_data'] = data_form['numberOfDays']

        if data_form['numberOfDays'] and (request.session['Account_Id'] is None):
            return redirect('dashboard/')
        elif request.session['Account_Id'] and data_form['numberOfDays']:
            return redirect('account/unresponsive/' + request.session['Account_Id']  + '/')
        else:
            return redirect('.')
    return redirect('.')
