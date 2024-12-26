from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers.auth_device_serializer import AuthDeviceSerializer

from Core.models.Device import Device

import logging

logger = logging.getLogger("device")


class AuthDeviceView(APIView):

    handler200 = Response(status=200)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попыткку позже'}, status=500)

    @swagger_auto_schema(
        operation_summary="Авторизация устройства",
        operation_description="Авторизирует текущее устройство по компании и идентификатору",
        tags=['login - Вход в систему'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
            'company': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='Компания'
            ),
            'code': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='Код устройства'
            ),
        },
        required=['company', 'code']  # Указываем, что оба поля обязательны
    ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'code': openapi.Schema(type=openapi.TYPE_STRING, description='Код устройства'),
                    }
                    ),
            400: openapi.Response(description="Устройство с таким идентификатором уже существует"),
            404: openapi.Response(description="Такого зарегистрированного устройства не найдено"),
            500: openapi.Response(description="Ошибка сервера"),
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            try:
                device = Device.objects.get(company__code=request.data.get('company'), code=request.data.get('code'))
            except:
                return Response({'detail': 'Такого зарегистрированного устройства не найдено, проверьте введённые данные или обратитесь к администратору'}, status=404)
            
            if device.counter == 1:
                logger.warning(f'Анонимный пользователь не смог войти в систему по причине существования устройства с таким кодом')
                return Response({'detail': 'Устройство с таким идентификатором уже существует'}, status=400)
            else:
                device.counter = 1
                device.save()
                logger.info(f'Анонимный пользователь зашёл в систему под устройством {request.data.get("code")}', extra={"device": request.data.get("code")})
                return Response({'code': request.data.get("code")}, status=200)
        except:
            raise self.handler500
