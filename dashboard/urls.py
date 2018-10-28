from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.show_all_accounts, name='account_name'),
    path('all', views.not_reported_for_two_days, name='unresponsive'),
    # path('account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
    # path('all_account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
]
