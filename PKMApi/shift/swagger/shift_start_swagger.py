from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from shift.views.shift_start_view import ShiftStartView

from Core.swagger_params import ACCESS_TOKEN_PARAM


class ShiftStartSwaggerView(ShiftStartView):
    @swagger_auto_schema(
            tags=['shift - Смена'],
            operation_summary='Внесение записи о начале смены',
            operation_description='Вносит запись о начале смены',
            manual_parameters=[ACCESS_TOKEN_PARAM],
            responses={
                200: 'Успешная обработка запроса',
                500: 'Ошибка сервера'
            }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
