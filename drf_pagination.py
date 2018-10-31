from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response


class AppPagination(PageNumberPagination):
    page_size = 10
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
