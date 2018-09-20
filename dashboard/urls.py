from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_device_info, name='device_health'),
    # path('account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
    # path('all_account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
]
