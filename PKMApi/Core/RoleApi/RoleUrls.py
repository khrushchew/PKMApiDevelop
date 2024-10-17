from django.urls import path

from .Views.RoleListCreateView import RoleListCreateApiView
from .Views.RoleRetrieveUpdateView import RoleRetrieveUpdateApiView

urlpatterns = [
    path('', RoleListCreateApiView.as_view()),
    path('detail/<int:pk>/', RoleRetrieveUpdateApiView.as_view()),
]