from django.urls import path

from .Views.AuthDeviceView import AuthDeviceApiView
from .Views.AuthUserView import AuthUserApiView

urlpatterns=[
    path('<str:company_code>/devices/', AuthDeviceApiView.as_view()),
    path('<str:company_code>/users/', AuthUserApiView.as_view())
]
