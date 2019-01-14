from django.urls import path, include

from . import views

app_name = 'get_days'

urlpatterns = [
    path('', views.days_html, name='days'),
    path('count', views.get_number_of_days, name='count'),
]

