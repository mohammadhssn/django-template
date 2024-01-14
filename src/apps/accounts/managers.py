from django.contrib.auth.models import BaseUserManager

from apps.utils.messages import (
    MESSAGE_ERROR_IS_ACTIVE_SUPERUSER, MESSAGE_ERROR_IS_STAFF_SUPERUSER, MESSAGE_ERROR_IS_SUPERUSER_SUPERUSER
)


class UserManager(BaseUserManager):

    def create_user(self, username: str, password: str, **extra_fields):
        """
        Creates a new user with the provided username and password.

        Parameters:
        - username (str): The username for the new user.
        - password (str): The password for the new user.
        - **extra_fields: Additional fields to be passed to the user model.

        Returns:
        - user: The newly created user object.
        """

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username: str, password: str, **extra_fields):
        """
        Creates a superuser with the given username, password, and extra fields.

        :param username: The username for the superuser. (str)
        :param password: The password for the superuser. (str)
        :param extra_fields: Additional fields for the superuser. (kwargs)
        :return: The created superuser. (User)
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(MESSAGE_ERROR_IS_STAFF_SUPERUSER)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(MESSAGE_ERROR_IS_SUPERUSER_SUPERUSER)
        if extra_fields.get('is_active') is not True:
            raise ValueError(MESSAGE_ERROR_IS_ACTIVE_SUPERUSER)

        return self.create_user(username, password, **extra_fields)
