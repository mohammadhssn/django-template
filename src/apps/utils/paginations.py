from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    """
    Custom pagination class that returns a consistent response format.

    This pagination class inherits from Django's `LimitOffsetPagination` class
    and overrides the `get_paginated_response()` method to return a response
    with a consistent format.

    The response format includes the following keys:
        - 'type': A string indicating the result type. Always set to 'success'.
        - 'count': An integer indicating the total number of results.
        - 'message': An optional message string. Always set to None.
        - 'result': The paginated result data.

    Example response format:
        {
            'type': 'success',
            'count': 100,
            'message': None,
            'result': [
                {'id': 1, 'name': 'foo'},
                {'id': 2, 'name': 'bar'},
                {'id': 3, 'name': 'baz'},
            ]
        }
    """

    def get_paginated_response(self, data) -> Response:
        """
        Returns a paginated response in the specified format.

        :param data: The paginated data to be included in the response.
        :type data: list or dict

        :return: A Response object containing paginated data.
        :rtype: Response
        """

        return Response(OrderedDict([('type', 'success'), ('count', self.count), ('message', None), ('result', data)]))
