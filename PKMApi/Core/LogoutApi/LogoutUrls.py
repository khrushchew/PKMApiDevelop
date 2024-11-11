from django.urls import path

from .Views.LogoutUserView import LogoutUserApiView

urlpatterns = [
    path('<str:company_code>/users/', LogoutUserApiView.as_view())
]