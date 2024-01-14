REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',],
    'EXCEPTION_HANDLER': 'apps.utils.exceptions.drf_exception_handler',
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATE_FORMAT': '%Y-%m-%d',
    'DEFAULT_PAGINATION_CLASS': 'apps.utils.paginations.CustomLimitOffsetPagination',
    'PAGE_SIZE': 15
}
