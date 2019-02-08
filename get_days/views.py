from django.shortcuts import render, redirect


def days_html(request):
    return render(request, 'get_days.html', content_type='text/html')


def get_number_of_days(request):
    if request.method == 'POST':
        data_form = request.POST
        request.session['temp_data'] = data_form['numberOfDays']

        if data_form['numberOfDays']:
            return redirect('dashboard/')
        else:
            return redirect('.')
    return redirect('.')
