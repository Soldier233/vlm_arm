from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView


def index(request):
    return HttpResponse("Agent Consumer Restful Service")


# /device/
class DeviceControlView(APIView):
    def get(self, request):
        pass
