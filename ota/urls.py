from django.urls import path

from . import views

app_name = 'ota'

urlpatterns = [
    path('reset', views.reset_device, name='reset'),
    path('ping', views.ping_device, name='ping'),
    path('apn', views.set_device_apn, name='apn'),
]