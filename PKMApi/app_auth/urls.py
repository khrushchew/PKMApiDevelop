from django.urls import path

from app_auth.views.auth_device_view import AuthDeviceView
from app_auth.views.custom_tokens_view import CustomTokenObtainPairView, CustomTokenRefreshView
from app_auth.views.auth_group_view import AuthGroupView

urlpatterns = [
    path('devices/', AuthDeviceView.as_view()),
    path('users/tokens/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/tokens_refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('users/groups/', AuthGroupView.as_view())
]
