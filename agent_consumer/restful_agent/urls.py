from django.urls import path

from .views import Heartbeat
from .views import ExecuteCommand

urlpatterns = [

    path('heartbeat/', Heartbeat.as_view(), name='heartbeat'),
    path('execute/', ExecuteCommand.as_view(), name='execute'),
]
