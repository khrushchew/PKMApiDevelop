from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..Serializers.AreaSerializer import AreaApiSerializer
from ..Serializers.AreaListSerializer import AreaListApiSerializer

from Core.models.Area import Area
from Core.models.Department import Department


class AreaApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_department(self):
        department_pk = self.request.data.get('department_pk')
        try:
            return Department.objects.get(pk=department_pk)
        except:
            raise NotFound({'error': 'Такого участка не найдено'})

    def get_area_list(self):
        filters = {'department__platform__company__code': self.kwargs.get('company_code')}
        opt_filters = ['department']
        for i in opt_filters:
            val = self.request.query_params.get('department')
            if val:
                filters[i] = val
        areas = Area.objects.filter(**filters).order_by('indent')
        if areas.exists():
            return areas
        else:
            raise NotFound({'error': 'Участков не найдено'})
        
    def get_area_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Area.objects.get(pk=pk)
        except:
            raise NotFound({'error': 'Такой площадки не найдено'})
    
    def create(self, request, *args, **kwargs):

        indent = request.data.get('indent')
        name = request.data.get('name')

        department = self.get_department()

        if Area.objects.filter(indent=indent, department__platform__company__code=department.platform.company.code).exists():
            raise ValidationError({'error': 'Участок с таким идентификатором уже существует'})
        
        if Area.objects.filter(name=name, department__platform__company__code=department.platform.company.code).exists():
            raise ValidationError({'error': 'Участок с таким названием уже существует'})
        
        try:
            Area.objects.create(indent=indent, name=name, department=department)
            return self.handler200
        except:
            return self.handler500
    
    def list(self, request, *args, **kwargs):
        areas = self.get_area_list()
        try:
            serializer = AreaListApiSerializer(areas, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def retrieve(self, request, *args, **kwargs):
        area = self.get_area_entity()
        try:
            serializer = AreaApiSerializer(area)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def partial_update(self, request, *args, **kwargs):
        indent = request.data.get('indent')
        name = request.data.get('name')
    
        area = self.get_area_entity()

        try:
            if indent:
                area.indent = indent
            if name:
                area.name = name
            if request.data.get('department_pk'):
                department = self.get_department()
                area.department = department
            area.save()
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
        