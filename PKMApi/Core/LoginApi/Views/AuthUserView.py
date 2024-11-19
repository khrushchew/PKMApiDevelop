import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..Rules import login_window

from Core.models.User import User

from ..Serializers.AuthUserSerializer import AuthUserApiSerializer


class AuthUserApiView(APIView):

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    company_code_param = openapi.Parameter(
        'company_code',  
        openapi.IN_PATH,
        description="Код компании",
        type=openapi.TYPE_STRING,
        required=True
    )

    @swagger_auto_schema(
        operation_summary="Авторизация пользователя",
        operation_description="Авторизирует пользователя по логину и паролю с учётом пройденного этапа авторизации по устройству",
        tags=['login'],
        manual_parameters=[company_code_param],
        request_body=AuthUserApiSerializer,
        responses={
            200: openapi.Response(description="Успешный ответ", examples={"window": "Табель", "token": "5d5a3448-9918-4a4c-a254-a7d15b05207f", "groups": ["Директор", "Кадровик"]}),
            400: openapi.Response(description="Устройство с таким идентификатором уже существует"),
            404: openapi.Response(description="Такого зарегистрированного устройства не найдено"),
            500: openapi.Response(description="Ошибка сервера"),
        },
    )
    def post(self, request, company_code):
        
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(company__code=company_code, username=username)
        except User.DoesNotExist:
            raise NotFound({'error': 'Такой пользователь не найден, проверьте введённые данные'})
        
        if not user.check_password(password):
            raise NotFound({'error': 'Неверный пароль, попробуйте снова'})
        
        if not user.is_active:
            raise NotFound({'error': 'Пользователь не активирован, обратитесь к кадровику или администратору'})

        if user.token:
            raise AuthenticationFailed({'error': 'Вход невозможен: активный сеанс уже существует'})

        new_token = str(uuid.uuid4())
        user.token = new_token
        user.save()

        groups = [group.name for group in user.groups.all()]

        login_window.update({'username': user.username, 'token': user.token, 'groups': groups,})
        return Response(login_window, status=200)
