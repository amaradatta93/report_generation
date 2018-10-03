from django.urls import path

from . import views

app_name = 'reports'

urlpatterns = [
    path('account_info/<int:account_key>/', views.account_contact, name='account_contact'),
    # path('all_account_info', views.all_device_and_billing_status, name='device_and_billing_status'),
    # path('device_info/<int:account_key>/', views.account_device_info, name='device_and_billing_status'),
    path('device_info/<int:account_key>/', views.account_device_info, name='device_and_billing_status'),
]
