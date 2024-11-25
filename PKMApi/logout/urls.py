from django.urls import path

from .swagger.logout_swagger import LogoutSwaggerView

urlpatterns = [
    path('', LogoutSwaggerView.as_view())
]