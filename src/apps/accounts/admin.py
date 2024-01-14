from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'is_active', 'is_staff')
    list_filter = ('is_staff',)

    fieldsets = (
        ('Main', {
            'fields': ('username', 'password')
        }),
        (
            'Permissions', {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'last_login', 'groups', 'user_permissions')
            }
        ),
    )

    add_fieldsets = ((None, {'fields': ('username', 'password1', 'password2')}),)

    search_fields = ('username',)
    filter_horizontal = ('groups', 'user_permissions')


# ---------------------------------------------------------------------------------------------------------------------
