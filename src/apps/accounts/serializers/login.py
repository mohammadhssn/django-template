from django.contrib.auth import get_user_model
from rest_framework import serializers


class LoginSerializer(serializers.ModelSerializer):
    """
        Serializer for the user authentication object
    """

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=150)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
