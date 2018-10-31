import sys

from django.conf import settings
from django.views.debug import technical_500_response


class SuperUserExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.ALLOWED_HOSTS:
            return technical_500_response(request, *sys.exc_info())


# class MyExceptionMiddleware(object):
#     def process_exception(self, request, exception):
#         if isinstance(exception, (InvalidSignatureError, ValidationError, ValidationError)):
#             return HttpResponse("{'msg','请重新登入'}", content_type='application/json')
#         return None
