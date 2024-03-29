from rest_framework import status
from rest_framework.exceptions import APIException, AuthenticationFailed, NotAuthenticated, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework_simplejwt.exceptions import InvalidToken

from apps.utils.messages import (
    MESSAGE_ERROR_NOT_AUTHENTICATED, MESSAGE_ERROR_OBJECTS_DOSE_NOT_EXISTS, MESSAGE_ERROR_PERMISSION_DENIED,
    MESSAGE_TOKEN_INVALID
)


def drf_exception_handler(exc, context) -> Response:
    """
    Exception handler for Django REST Framework.

    :param exc: The exception object that was raised.
    :type exc: Exception

    :param context: The context in which the exception was raised.
    :type context: dict

    :return: The response generated by the exception handler.
    :rtype: Response
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(
        exc, (NotAuthenticated, PermissionDenied, InvalidToken, AuthenticationFailed, ObjectDoesNotExistException)
    ):
        response.data.clear()
        response.data['type'] = 'error'
        response.data['count'] = None

        if isinstance(exc, NotAuthenticated):
            response.data['message'] = MESSAGE_ERROR_NOT_AUTHENTICATED
        elif isinstance(exc, PermissionDenied):
            response.data['message'] = MESSAGE_ERROR_PERMISSION_DENIED
        elif isinstance(exc, InvalidToken):
            response.data['message'] = MESSAGE_TOKEN_INVALID
        elif isinstance(exc, AuthenticationFailed):
            response.data['message'] = MESSAGE_TOKEN_INVALID
        elif isinstance(exc, ObjectDoesNotExistException):
            response.data['message'] = MESSAGE_ERROR_OBJECTS_DOSE_NOT_EXISTS

        response.data['result'] = None

    return response


class ObjectDoesNotExistException(APIException):
    """
    Custom exception used for cases where an object does not exist.

    Inherits from the `APIException` class which is a subclass of Django's `Exception` class.

    Attributes:
        status_code (int): The HTTP status code to be returned.
        default_detail (dict): A dictionary that contains a default detail message with the following keys:
            - type: A string indicating the type of error.
            - count: An integer indicating the count of affected objects.
            - message: A string indicating the error message.
            - result: A dictionary containing the result (if any).
        default_code (str): A string indicating the default error code.
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = {'type': 'error', 'count': None, 'message': MESSAGE_ERROR_OBJECTS_DOSE_NOT_EXISTS, 'result': None}
    default_code = 'error'
