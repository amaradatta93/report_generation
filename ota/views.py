from django.http import HttpResponse

from dashboard.models import DeviceQueue
from .reset_utils import reset_command, get_date_time_sent


def reset_device(request):
    imei_number = request.GET.get('imei_number'),
    device_name = request.GET.get('device_name'),
    command = reset_command(imei_number, device_name)
    date_sent, time_sent = get_date_time_sent()

    reset_queue = DeviceQueue()

    reset_queue.imei = imei_number
    reset_queue.command = command
    reset_queue.date_stamp = date_sent
    reset_queue.time_stamp = time_sent
    reset_queue.command_status = 1

    try:
        reset_queue.save()
        return HttpResponse('Success')
    except Exception as e:
        return HttpResponse(e)


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
