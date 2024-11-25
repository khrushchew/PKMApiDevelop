from django.urls import path, include

from rest_framework import routers

from about.swagger.about_swagger import AboutSwaggerView

about_router = routers.SimpleRouter()
about_router.register(r'', AboutSwaggerView, 'about')

urlpatterns = [
    path('', include(about_router.urls))
]