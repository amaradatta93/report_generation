from django.urls import path

from . import views

app_name = 'reports'

urlpatterns = [
    path('unresponsive/<int:account_key>/', views.not_reported_for_two_days, name='unresponsive'),
    path('days', views.days_html, name='days'),
    path('numberCount ', views.get_number_of_days, name='get_number_of_days'),
]
