from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.show_all_accounts, name='account_name'),
    path('all', views.not_reported_for_two_days, name='unresponsive'),
]
