import json

from rest_framework.status import is_success


class ResultMiddleware(object):
    def process_response(self, request, response):
        if hasattr(response, 'data'):
            if isinstance(response.data, dict):
                if is_success(response.status_code):
                    response.data.update({"code": 1, "msg": "请求成功"})
                else:
                    response.data.update({"code": 0, "msg": "请求失败"})
            if isinstance(response.data, str):
                msg = response.data
                response.data = {"msg": msg, "code": 1}
                if is_success(response.status_code):
                    pass
                else:
                    response.data.update({"code": 0, })
            response.content = json.dumps(response.data)
        return response
