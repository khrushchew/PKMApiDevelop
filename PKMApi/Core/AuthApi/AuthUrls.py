from django.urls import path
from .AuthViews import AuthApiView


urlpatterns=[
    path('user/<str:company_code>/', AuthApiView.as_view()),
]
