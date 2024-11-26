from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from rest_framework.exceptions import NotFound

from subdivision.serializers.subdivision_create_serializer import SubdivisionCreateSerializer
from subdivision.serializers.subdivision_list_serializer import SubdivisionListSerializer
from subdivision.serializers.subdivision_retrieve_serializer import SubdivisionRetrieveSerializer
from subdivision.serializers.subdivision_update_serializer import SubdivisionUpdateSerializer

from Core.models.Subdivision import Subdivision
from Core.models.Company import Company
from Core.models.User import User

class SubdivisionView(ViewSet):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler201 = Response({'detail': 'Подразделение успешно создано'}, status=201)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_subdivision_list(self):
        try:
            return Subdivision.objects.filter(company=self.request.user.company).order_by('name')
        except:
            raise NotFound({'detail': 'Подразделений не найдено'})
    
    def get_subdivision_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Subdivision.objects.get(pk=pk)
        except:
            raise NotFound({'detail': 'Такого подразделения не найдено'})

    access_token_param = openapi.Parameter(
        'access_token',
        openapi.IN_HEADER,
        description="Токен доступа",
        type=openapi.TYPE_STRING,
        required=True,
        default='JWT {token}'
    )

    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Создание подразделения',
        operation_description='Создаёт подразделение для определённой компании',
        manual_parameters=[access_token_param],
        request_body=SubdivisionCreateSerializer,
        responses={
            201: "Успешное создание подразделения",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def create(self, request, *args, **kwargs):

        data = request.data
        data['company'] = request.user.company.pk

        serializer = SubdivisionCreateSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        try:    
            serializer.save()
            return self.handler201
        except:
            return self.handler500
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Вывод списка подразделений',
        operation_description='Выводит список подразделений для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def list(self, request, *args, **kwargs):
        subdivisions = self.get_subdivision_list()

        serializer = SubdivisionListSerializer(subdivisions, many=True)

        if serializer.data:
            for i in range(1, len(serializer.data) + 1):
                serializer.data[i - 1].setdefault("indent", i)

        data = serializer.data
        data.append({'indent': 0, 'name': 'Резерв', 'users': User.objects.filter(subdivision=None).count()})
        
        return Response(sorted(data, key=lambda i: i["indent"]), status=200)
        # except:
        #     return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)
    
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Вывод определённого подразделения',
        operation_description='Выводит определённое подразделение для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def retrieve(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            serializer = SubdivisionRetrieveApiSerializer(subdivision)
            return Response(serializer.data, status=200)
        except:
            return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Изменение определённого подразделения',
        operation_description='Изменяет определённое подразделение для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def update(self, request, *args, **kwargs):
        
        subdivision = self.get_subdivision_entity()

        self.check_name()

        serializer = SubdivisionUpdateApiSerializer(subdivision, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response(status=200)
        except:
            return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    @swagger_auto_schema(
        tags=['subdivision - Подразделение'],
        operation_summary='Удаление определённого подразделения',
        operation_description='Удаляет определённое подразделение для определённой компании',
        manual_parameters=[access_token_param],
        responses={
            200: "Успешная обработка запроса",
            400: "Ошибка при обработке запроса",
            500: "Ошибка сервера",
        }
    )
    def destroy(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            subdivision.delete()
            return Response(status=200)
        except:
            return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        