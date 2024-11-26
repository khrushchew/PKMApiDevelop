from django.urls import path, include

from rest_framework import routers

from .views.subdivision_view import SubdivisionView

subdivision_router = routers.SimpleRouter()
subdivision_router.register(r'', SubdivisionView, 'subdivision')

urlpatterns = [
    path('', include(subdivision_router.urls))
]