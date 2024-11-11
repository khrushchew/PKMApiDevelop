from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..Serializers.PlatformSerializer import PlatformApiSerializer

from Core.models.Company import Company
from Core.models.Platform import Platform


class PlatformApiViewSet(ViewSet):

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code).pk
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
    
    def get_platform_list(self):
        try:
            return Platform.objects.filter(company__code=self.kwargs.get('company_code'))
        except:
            raise NotFound({'error': 'Площадок не найдено'})
    
    def get_platform_entity(self):
        try:
            return Platform.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такой площадки не найдено'})

    def check_name(self):
        if Platform.objects.filter(name=self.request.data.get('name'), company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Площадка с таким названием уже существует'})
    
    def check_indent(self):
        if Platform.objects.filter(indent=self.request.data.get('indent'), company__code=self.kwargs.get('company_code')).exists():
            raise ValidationError({'error': 'Площадка с таким идентификатором уже существует'})
        
    def create(self, request, *args, **kwargs):

        data = request.data

        data["company"] = self.get_company()

        self.check_name()
        self.check_indent()

        try:
            serializer = PlatformApiSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return self.handler201
            else:
                return Response(serializer.errors, status=400)
        except:
            return self.handler500
    
    def list(self, request, *args, **kwargs):

        platforms = self.get_platform_list()

        try:
            serializer = PlatformApiSerializer(platforms, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def retrieve(self, request,  *args, **kwargs):
        platform = self.get_platform_entity()
        try:
            serializer = PlatformApiSerializer(platform)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
        
    def update(self, request, *args, **kwargs):

        data = request.data

        self.check_name()
        self.check_indent()

        platform = self.get_platform_entity()

        try:
            serializer = PlatformApiSerializer(platform, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            else:
                return Response(serializer.errors, status=400)
        except:
            return self.handler500
        
    def destroy(self, request, *args, **kwargs):
        platform = self.get_platform_entity()

        try:
            platform.delete()
            return Response(status=200)
        except:
            return self.handler500
    