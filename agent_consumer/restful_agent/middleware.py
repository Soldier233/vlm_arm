from django.http import JsonResponse
from django.apps import apps
from .common.api_response import ApiResponse


class HeaderCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # 获取配置
        self.config = apps.get_app_config('restful_agent').config

    def __call__(self, request):
        # 你可以在这里使用 self.config
        print("Current config:", self.config)

        auth_code = request.headers.get('Authorization')
        if auth_code != self.config.get('secret'):
            return ApiResponse(message='No Permission', success=False, status=403)

        response = self.get_response(request)
        return response
