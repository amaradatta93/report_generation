from django.shortcuts import render

from dashboard.models import DeviceQueue
from .ota_utils import reset_command, ping_command, apn_command, get_date_time_sent


def reset_device(request):
    imei_number = request.GET.get('imei_number')
    device_name = request.GET.get('device_name')
    account_id = request.GET.get('account_id')

    command = reset_command(imei_number, device_name)
    date_sent, time_sent = get_date_time_sent()

    if command:
        reset_queue = DeviceQueue()
        reset_queue.imei = imei_number
        reset_queue.command = command
        reset_queue.date_stamp = date_sent
        reset_queue.time_stamp = time_sent
        reset_queue.command_status = 1

        try:
            reset_queue.save()
            status = 'Success'
        except Exception as e:
            status = e
    else:
        status = ' - Contact infospectrum'

    return render(request, 'ota_success.html', {'account_id': account_id, 'status': status, 'command': 'Reset'})


def ping_device(request):
    imei_number = request.GET.get('imei_number')
    device_name = request.GET.get('device_name')
    account_id = request.GET.get('account_id')

    command = ping_command(imei_number, device_name)
    date_sent, time_sent = get_date_time_sent()

    if command:
        reset_queue = DeviceQueue()
        reset_queue.imei = imei_number
        reset_queue.command = command
        reset_queue.date_stamp = date_sent
        reset_queue.time_stamp = time_sent
        reset_queue.command_status = 1

        try:
            reset_queue.save()
            status = 'Success'
        except Exception as e:
            status = e
    else:
        status = ' - Contact infospectrum'

    return render(request, 'ota_success.html', {'account_id': account_id, 'status': status, 'command': 'Ping'})


def set_device_apn(request):
    imei_number = request.GET.get('imei_number')
    device_name = request.GET.get('device_name')
    account_id = request.GET.get('account_id')

    command = apn_command(imei_number, device_name)
    date_sent, time_sent = get_date_time_sent()

    if command:
        reset_queue = DeviceQueue()
        reset_queue.imei = imei_number
        reset_queue.command = command
        reset_queue.date_stamp = date_sent
        reset_queue.time_stamp = time_sent
        reset_queue.command_status = 1

        try:
            reset_queue.save()
            status = 'Success'
        except Exception as e:
            status = e
    else:
        status = ' - Contact infospectrum'

    return render(request, 'ota_success.html', {'account_id': account_id, 'status': status, 'command': 'APN'})
