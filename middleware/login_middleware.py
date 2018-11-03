from uuid import uuid4

from django.http import HttpResponse
from jwt import InvalidSignatureError
from rest_framework.exceptions import ValidationError
from rest_framework.status import is_success
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


# 1.每次登录 response 处理 记录 jwt
# 2.每次请求判断 jwt是否与表中相等(相当于 用户 异设备登录获取了新的jwt)  不等 就修改uuid

# 详 见 https://blog.csdn.net/qq_33042187/article/details/83347337


class ValidTokenMiddleware(object):
    def process_request(self, request):
        jwt_token = request.META.get('HTTP_AUTHORIZATION', None)
        if jwt_token:
            data = {
                'token': request.META['HTTP_AUTHORIZATION'].split(' ')[1],
            }
            try:
                valid_data = VerifyJSONWebTokenSerializer().validate(data)
                user = valid_data['user']
            except (InvalidSignatureError, ValidationError):
                # 找不到用户
                return HttpResponse("{'msg','请重新登入'}", content_type='application/json')
            if user.user_jwt != data['token']:
                user.user_secret = uuid4()
                user.save()
                return HttpResponse("{'msg','请重新登入'}", content_type='application/json')

    def process_response(self, request, response):
        if request.META['PATH_INFO'] == '/login/':
            if is_success(response.status_code):
                rep_data = response.data
                valid_data = VerifyJSONWebTokenSerializer().validate(rep_data)
                user = valid_data['user']
                user.user_jwt = rep_data['token']
                user.save()
                return response
            else:
                return response
        else:
            return response
