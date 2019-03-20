from django.urls import path

from . import views

app_name = 'ota'

urlpatterns = [
    path('command', views.send_command, name='send_command'),
]