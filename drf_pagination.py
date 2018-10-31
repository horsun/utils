from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response


# Usage
#       在接口中添加下面代码
#     pagination_class = AppPagination
# 或者在setting中的 drf设置里面添加
#      'DEFAULT_PAGINATION_CLASS': '你的目录.AppPagination'
# url：    X.X.X.X/books/?page=1&pageSize=10
class AppPagination(PageNumberPagination):
    page_size = 10  # 如果url parm 没有pageSize 参数 就默认为10
    page_query_param = 'page'
    page_size_query_description = 'pageSize'
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        return Response({
            # 'limit': self.page_size,
            'list': data,
            'total_pages': self.page.paginator.num_pages,
            'next': bool(self.page.number < self.page.paginator.num_pages)
        })
