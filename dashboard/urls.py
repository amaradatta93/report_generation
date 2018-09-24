from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.all_device_info, name='device_health'),
    path('unresponsive/', views.not_reported_for_two_days, name='unresponsive')
    # path('account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
    # path('all_account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
]
