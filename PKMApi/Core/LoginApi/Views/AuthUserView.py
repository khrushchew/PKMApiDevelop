from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from Core.models.User import User
from ..Serializers.AuthUserSerializer import AuthUserApiSerializer


class AuthUserApiView(APIView):

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
            200: 'Вывод групп пользователя',
            401: 'Ошибка входа'
        }
    )
    def post(self, request):

        user = request.user
        
        if user.session:
            raise AuthenticationFailed({'detail': 'Такой пользователь уже активен на другом устройстве'})

        user.session = True
        user.save()

        return Response({
                'groups': [group.name for group in user.groups.all()],
            }, status=200)
