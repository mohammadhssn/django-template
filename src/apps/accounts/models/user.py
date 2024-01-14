from django.contrib.auth.models import AbstractUser

from apps.accounts.managers import UserManager


class User(AbstractUser):
    email = None
    first_name = None
    last_name = None
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS: list = []

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
