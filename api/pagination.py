from rest_framework.pagination import CursorPagination


class CustomCursorPagination(CursorPagination):
    page_size = 1
    ordering = 'name'
    cursor_query_param = 'next'
