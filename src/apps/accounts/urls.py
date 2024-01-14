from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.accounts.views import login

app_name = 'accounts'
router = SimpleRouter()

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='login'),
    path('token_refresh/', login.TokenRefreshView.as_view(), name='token_refresh'),
    # Router
    path('', include(router.urls)),
]
