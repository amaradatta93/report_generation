from django.shortcuts import render
from dashboard.models import DeviceRegister, DeviceType

import json


def send_command(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name')
    }
    return render(request, 'commands.html', {'response': response})
