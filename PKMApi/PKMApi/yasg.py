from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import SessionAuthentication

schema_view = get_schema_view(
   openapi.Info(
      title="API приложения Master Plan",
      default_version='0.1.0',
      description="Здесь расположены все ручки для управления приложением",
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=(permissions.IsAdminUser,),
   authentication_classes=(SessionAuthentication,),
)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
