from django.urls import path

from .Views.AuthDeviceView import AuthDeviceApiView
from .Views.AuthUserView import AuthUserApiView

from .Views.CustomTokensView import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns=[
    path('devices/', AuthDeviceApiView.as_view()),

    path('users/tokens/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/tokens_refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    path('users/groups/', AuthUserApiView.as_view())
]
