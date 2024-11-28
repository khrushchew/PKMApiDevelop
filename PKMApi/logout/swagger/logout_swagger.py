from logout.views.logout_view import LogoutView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class LogoutSwaggerView(LogoutView):
    access_token_param = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description='Токен доступа',
        type=openapi.TYPE_STRING,
        required=True,
        default='JWT {token}'
    )

    @swagger_auto_schema(
        tags=['logout - Выход из системы'],
        operation_summary='Выход пользователя из системы (Доступно только при наличии access токена)',
        operation_description='Выводит пользователя из системы. НА УСТРОЙСТВЕ УДАЛЯЮТСЯ ACCESS И REFRESH ТОКЕНЫ',
        manual_parameters=[access_token_param],
        responses={
            200: 'Выход из системы',
            401: 'Ошибка выхода'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
