from django.urls import path
from .AuthViews import AuthApiView


urlpatterns=[
    path('user/', AuthApiView.as_view()),
]
