from django.urls import path

from .Views.PlatformListCreateView import PlatformListCreateApiView
from .Views.PlatformRetrieveUpdateView import PlatformRetrieveUpdateApiView

urlpatterns=[
    path('', PlatformListCreateApiView.as_view()),
    path('detail/<int:pk>/', PlatformRetrieveUpdateApiView.as_view())
]