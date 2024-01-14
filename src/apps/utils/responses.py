from rest_framework.response import Response

VALID_RESPONSE_TYPES = ['success', 'error', 'warning']


class TemplateResponse(Response):
    """
    This is the common http response template
    across all projects of Ryca LLC.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes a new instance of the class.

        Parameters:
            **kwargs (dict): Additional keyword arguments.

        Keyword Arguments:
            type (str): The type of the response. Defaults to 'success'.
            count (int): The count of the response.
            message (str): The message of the response.
            result (str): The result of the response.

        Raises:
            ValueError: If the specified response type is not valid.
        """
        type_ = kwargs.pop('type', 'success')

        if type_ not in VALID_RESPONSE_TYPES:
            raise ValueError("'%s' is not a valid response type." % type_)

        kwargs['data'] = {
            'type': type_,
            'count': kwargs.pop('count', None),
            'message': kwargs.pop('message', None),
            'result': kwargs.pop('result', None),
        }
        super().__init__(**kwargs)
