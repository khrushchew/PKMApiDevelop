from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..serializers.area_retrieve_serializer import AreaRetrieveSerializer
from ..serializers.area_list_serializer import AreaListSerializer
from ..serializers.area_create_serializer import AreaCreateSerializer

from Core.models.Area import Area
from Core.models.Department import Department


class AreaView(ViewSet):

    permission_classes = [IsAuthenticated]

    handler201 = Response(status=201)
    handler200 = Response(status=200)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_department(self):
        department_pk = self.request.data.get('department_pk')
        try:
            return Department.objects.get(pk=department_pk)
        except:
            raise NotFound({'detail': 'Такого участка не найдено'})

    def get_area_list(self):
        filters = {'department__platform__company': self.request.user.company}
        opt_filters = ['department']
        for i in opt_filters:
            val = self.request.query_params.get('department')
            if val:
                filters[i] = val
        areas = Area.objects.filter(**filters).order_by('indent')
        if areas.exists():
            return areas
        else:
            raise NotFound({'detail': 'Участков не найдено'})
        
    def get_area_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Area.objects.get(pk=pk)
        except:
            raise NotFound({'detail': 'Такой площадки не найдено'})
    
    def check_indent(self):
        if Area.objects.filter(indent=self.request.data.get('indent'), department__platform__company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Участок с таким идентификатором уже существует'})

    def check_name(self):
        if Area.objects.filter(name=self.request.data.get('name'), department__platform__company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Участок с таким названием уже существует'})

    def create(self, request, *args, **kwargs):

        self.check_indent()
        self.check_name()

        serializer = AreaCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.handler201
        except:
            return self.handler500
        
    def list(self, request, *args, **kwargs):
        areas = self.get_area_list()
        try:
            serializer = AreaListSerializer(areas, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def retrieve(self, request, *args, **kwargs):
        area = self.get_area_entity()
        try:
            serializer = AreaRetrieveSerializer(area)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def update(self, request, *args, **kwargs):
        
        data = request.data
        
        self.check_indent()
        self.check_indent()

        area = self.get_area_entity()

        serializer = AreaCreateSerializer(area, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return self.handler200
        except:
            return self.handler500
    
    def destroy(self, request, *args, **kwargs):
        area = self.get_area_entity()
        try:
            area.delete()
            return self.handler200
        except:
            return self.handler500
        