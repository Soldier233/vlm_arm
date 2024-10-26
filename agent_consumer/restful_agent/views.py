import time

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView

from .common.api_response import ApiResponse


class Heartbeat(APIView):
    def post(self, request):
        return ApiResponse(message=str(time.time()))


class ExecuteCommand(APIView):
    def post(self, request):
        command = request.data.get('command')
        # Simulate command execution
        return ApiResponse(message='Command executed', data={'command': command})
