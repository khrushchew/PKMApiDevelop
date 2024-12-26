from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import logging
logger = logging.getLogger('auth_user')

class CustomTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_summary="Получение пары токенов",
        operation_description="Возвращает пару токенов: access и refresh для аутентификации.",
        tags=["login - Вход в систему"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Имя пользователя'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль'),
            },
            required=['username', 'password'],
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh токен'),
                    'access': openapi.Schema(type=openapi.TYPE_STRING, description='Access токен'),
                }
            ),
            401: "Учетные данные неверны или отсутствуют",
        }
    )
    def post(self, request, *args, **kwargs):
        logger.info(f'Пользователь входит в систему под именем {request.data.get("username")}', extra={'username': request.data.get("username")})
        return super().post(request, *args, **kwargs)

class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        operation_summary="Обновление access токена",
        operation_description="Обновляет access токен с использованием refresh токена.",
        tags=["login - Вход в систему"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh токен'),
            },
            required=['refresh'],
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING, description='Новый access токен'),
                }
            ),
            401: "Refresh токен недействителен или истек",
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
