from django.http import JsonResponse


class ApiResponse(JsonResponse):
    def __init__(self, data=None, message='', status=200, success=True, **kwargs):
        content = {
            'success': success,
            'message': message,
            'data': data
        }
        super().__init__(content, status=status, **kwargs)
