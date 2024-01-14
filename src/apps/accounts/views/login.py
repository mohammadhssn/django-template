from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from apps.accounts.serializers.login import LoginSerializer
from apps.utils.messages import MESSAGE_ERROR_USER_NOT_ACTIVE, MESSAGE_LOGIN_ERROR, MESSAGE_TOKEN_INVALID
from apps.utils.responses import TemplateResponse


class LoginView(CreateAPIView):
    """
    A view for user login. Authenticates the user's credentials and generates access and refresh tokens upon success.

    Required POST Parameters:
    - username: The username of the user.
    - password: The password associated with the username.

    Returns:
    On successful login:
    {
        'type': 'success',
        'result': {
            'username': str,
            'access_token': str,
            'refresh_token': str
        },
        'status': HTTP_200_OK
    }

    On unsuccessful login:
    {
        'type': 'error',
        'message': str,
        'status': HTTP_401_UNAUTHORIZED or HTTP_400_BAD_REQUEST
    }
    """

    permission_classes = ()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs) -> TemplateResponse:
        """
        Handles the HTTP POST request and creates a new resource.

        :param:
            request (HttpRequest): The HTTP request object.
            args (tuple): Additional positional arguments.
            kwargs (dict): Additional keyword arguments.

        :return:
            RycaResponse: The HTTP response object.
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            username = validated_data.get('username')
            password = validated_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:  # check if user is active return error
                    return TemplateResponse(
                        type='error', message=MESSAGE_ERROR_USER_NOT_ACTIVE, status=status.HTTP_401_UNAUTHORIZED
                    )

                update_last_login(sender=get_user_model(), user=user)  # Set user's last login.
                refresh = RefreshToken.for_user(user)
                data = {
                    'username': user.username,
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                }
                return TemplateResponse(type='success', result=data, status=status.HTTP_200_OK)
            else:
                return TemplateResponse(type='error', message=MESSAGE_LOGIN_ERROR, status=status.HTTP_401_UNAUTHORIZED)
        return TemplateResponse(type='error', message=MESSAGE_LOGIN_ERROR, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------------------------------------------------------------


class TokenRefreshView(TokenViewBase):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs) -> TemplateResponse:
        """
        Handles the HTTP POST request for the API endpoint.

        Parameters:
            request (Request): The HTTP request object.
            args (Tuple): Additional positional arguments.
            kwargs (Dict): Additional keyword arguments.

        Returns:
            TemplateResponse: The response object containing the result of the request.

        Raises:
            TokenError: If there is an error with the token.

        """

        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid():
                return TemplateResponse(type='success', result=serializer.validated_data, status=status.HTTP_200_OK)
            return TemplateResponse(type='error', message=MESSAGE_TOKEN_INVALID, status=status.HTTP_401_UNAUTHORIZED)
        except TokenError:
            return TemplateResponse(type='error', message=MESSAGE_TOKEN_INVALID, status=status.HTTP_401_UNAUTHORIZED)
