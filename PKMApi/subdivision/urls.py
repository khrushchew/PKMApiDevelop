from django.urls import path, include

from rest_framework import routers

from subdivision.swagger.subdivision_swagger_view import SubdivisionSwaggerView

subdivision_router = routers.SimpleRouter()
subdivision_router.register(r'', SubdivisionSwaggerView, 'subdivision')

urlpatterns = [
    path('', include(subdivision_router.urls))
]