from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..Serializers.LogoutUserSerializer import LogoutUserApiSerializer

from Core.models.User import User

from rest_framework_simplejwt.tokens import RefreshToken


class LogoutUserApiView(APIView):
    
    permission_classes = [IsAuthenticated]

    access_token_param = openapi.Parameter(
        'access',
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
        user = request.user
        
        user.session = False
        user.save()

        return Response({'detail': 'Вы успешно вышли из системы!'}, status=200)