from django.http import HttpResponse

from .reset_utils import reset_command


def reset_device(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name'),
        'command': reset_command(request.GET.get('imei_number'), request.GET.get('device_name'))
    }

    return HttpResponse(response.values())


def ping_device(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name'),
    }

    return HttpResponse(response.values())


def set_device_apn(request):
    response = {
        'imei_number': request.GET.get('imei_number'),
        'device_name': request.GET.get('device_name'),
    }

    return HttpResponse(response.values())
