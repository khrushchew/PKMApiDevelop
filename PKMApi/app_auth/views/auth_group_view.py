from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from Core.models.User import User
from ..serializers.auth_group_serializer import AuthGroupSerializer

from django.utils import timezone

import logging
logger = logging.getLogger('auth_group')


class AuthGroupView(APIView):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    access_token_param = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description='Токен доступа',
        type=openapi.TYPE_STRING,
        required=True,
        default='JWT {token}'
    )

    @swagger_auto_schema(
        tags=['login - Вход в систему'],
        operation_summary='Получение групп пользователя (Доступно только при наличии access токена)',
        operation_description='Получает все доступные группы пользователя',
        manual_parameters=[access_token_param],
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=
            {
                "groups": openapi.Schema(type=openapi.TYPE_ARRAY, description='Список групп', items=openapi.Items(type=openapi.TYPE_STRING)),
                "start_shift": openapi.Schema(type=openapi.TYPE_STRING, description='Время начала смены'),
                "end_shift": openapi.Schema(type=openapi.TYPE_STRING, description='Время конца смены'),
                "time_now": openapi.Schema(type=openapi.TYPE_STRING, description='Текущее время'),
            }       
            ),
            401: 'Ошибка входа'
        }
    )
    def post(self, request):

        user = request.user
        
        if user.session:
            logger.warning(f"Пользователь {request.user.username} попытался войти в приложение, но у него есть активные сеансы", extra={'username': request.user.username})
            raise AuthenticationFailed({'detail': 'Такой пользователь уже активен на другом устройстве'})

        user.session = True
        user.save()

        if user.start_shift:
            start_shift = user.start_shift.strftime('%d-%m-%Y %H:%M:%S')
        else:
            start_shift = None

        if user.end_shift:
            end_shift = user.end_shift.strftime('%d-%m-%Y %H:%M:%S')
        else:
            end_shift = None

        logger.info(f"Пользователь {request.user.username} вошёл в приложение", extra={'username': request.user.username})

        return Response({
                'groups': [group.name for group in user.groups.all()],
                'start_shift': start_shift,
                'end_shift': end_shift,
                'time_now': timezone.now().strftime('%d-%m-%Y %H:%M:%S'),
            }, status=200)
