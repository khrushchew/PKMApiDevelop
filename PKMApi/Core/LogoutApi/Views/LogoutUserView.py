from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..Serializers.LogoutUserSerializer import LogoutUserApiSerializer

from Core.models.User import User


class LogoutUserApiView(APIView):

    company_code_param = openapi.Parameter(
        'company_code',  
        openapi.IN_PATH,
        description="Код компании",
        type=openapi.TYPE_STRING,
        required=True
    )

    @swagger_auto_schema(
        operation_summary="Завершение сеанса пользователя",
        operation_description="Завершает текущий сеанс пользователя, обнуляя существующий токен",
        tags=['logout'],
        manual_parameters=[company_code_param],
        request_body=LogoutUserApiSerializer,
        responses={
            200: openapi.Response(description="Успешный ответ"),
            404: openapi.Response(description="Такого пользователя не найдено"),
        },
    )

    def post(self, request, company_code):

        username = request.data.get('username')

        try:
            user = User.objects.get(company__code=company_code, username=username)
        except:
            raise NotFound({'error': 'Такой пользователь не найден, проверьте введённые данные'})
        
        user.token = None
        user.save()

        return Response({'message': 'Вы успешно вышли из системы'}, status=200)
