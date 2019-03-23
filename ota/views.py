from django.http import HttpResponse


def reset_device(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name'),
        'command': 'reset'
    }

    return HttpResponse(response.values())


def ping_device(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name'),
        'command': 'pinging'
    }

    return HttpResponse(response.values())


def set_device_apn(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name'),
        'command': 'set apn'
    }

    return HttpResponse(response.values())
