from django.http import HttpResponse, JsonResponse

from .utils import get_device_info


def all_device_info(request, account_id=None):
    device_info = get_device_info(account_id)
    output = []
    for device in device_info:
        output.append({'imei': device.imei})
    return JsonResponse({'Device': output})
