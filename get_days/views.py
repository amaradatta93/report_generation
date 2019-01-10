from django.shortcuts import render

threshold = 0


def days_html(request):
    return render(request, 'get_days.html', content_type='text/html')


def get_number_of_days(request):
    if request.method == 'POST':
        data_form = request.POST
        days = data_form['numberOfDays']
        threshold = days
    return threshold


def pass_days():
    return threshold
