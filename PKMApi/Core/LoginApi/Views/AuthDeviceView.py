from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..Serializers.AuthDeviceSerializer import AuthDeviceApiSerializer

from Core.models.Device import Device

class AuthDeviceApiView(APIView):

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попыткку позже'}, status=500)

    @swagger_auto_schema(
        operation_summary="Авторизация устройства",
        operation_description="Авторизирует текущее устройство по компании и идентификатору",
        tags=['login - Вход в систему'],
        request_body=AuthDeviceApiSerializer,
        responses={
            200: openapi.Response(description="Успешный ответ и возврат кода устройства"),
            400: openapi.Response(description="Устройство с таким идентификатором уже существует"),
            404: openapi.Response(description="Такого зарегистрированного устройства не найдено"),
            500: openapi.Response(description="Ошибка сервера"),
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            try:
                device = Device.objects.get(company__code=request.data.get('company_code'), code=request.data.get('code'))
            except:
                return Response({'detail': 'Такого зарегистрированного устройства не найдено, проверьте введённые данные или обратитесь к администратору'}, status=404)
            
            if device.counter == 1:
                return Response({'detail': 'Устройство с таким идентификатором уже существует'}, status=400)
            else:
                device.counter = 1
                device.save()
                return Response({'code': request.data.get("code")}, status=200)
        except:
            raise self.handler500
