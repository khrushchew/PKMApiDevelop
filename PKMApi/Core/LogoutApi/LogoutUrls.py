from django.urls import path

from .Views.LogoutUserView import LogoutUserApiView

urlpatterns = [
    path('users/', LogoutUserApiView.as_view())
]