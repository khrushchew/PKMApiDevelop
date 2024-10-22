from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ModelViewSet

from ..Serializers.PlatformSerializer import PlatformApiSerializer

from Core.models.Company import Company
from Core.models.Platform import Platform


class PlatformApiViewSet(ModelViewSet):

    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    serializer_class = PlatformApiSerializer

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
    
    def get_platform_list(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Platform.objects.filter(company__code=company_code)
        except:
            raise NotFound({'error': 'Площадок не найдено'})
    
    def get_platform_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Platform.objects.get(pk=pk)
        except:
            raise NotFound({'error': 'Такой площадки не найдено'})

    def create(self, request, *args, **kwargs):
        indent = request.data.get('indent')
        name = request.data.get('name')
        address = request.data.get('address')

        company = self.get_company()

        if Platform.objects.filter(name=name, company__code=company.code).exists():
            raise ValidationError({'error': 'Площадка с таким названием уже существует'}, status=409)
        
        if Platform.objects.filter(indent=indent, company__code=company.code).exists():
            raise ValidationError({'error': 'Площадка с таким идентификатором уже существует'}, status=409)

        try:
            Platform.objects.create(indent=indent, name=name, address=address, company=company)
            return Response(status=200)
        except:
            return self.handler500
    
    def list(self, request, *args, **kwargs):
        platforms = self.get_platform_list()

        try:
            serializer = self.get_serializer(platforms, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def retrieve(self, request,  *args, **kwargs):
        platform = self.get_platform_entity()
        try:
            serializer = self.get_serializer(platform)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
        
    def partial_update(self, request, *args, **kwargs):
        indent = request.data.get('indent')
        name = request.data.get('name')
        address = request.data.get('address')

        platform = self.get_platform_entity()
        
        if Platform.objects.filter(name=name, company__code=platform.company.code).exists():
            raise ValidationError({'error': 'Площадка с таким названием уже существует'}, status=409)
        
        if Platform.objects.filter(indent=indent, company__code=platform.company.code).exists():
            raise ValidationError({'error': 'Площадка с таким идентификатором уже существует'}, status=409)

        try:
            if indent:
                platform.indent = indent
            if name:
                platform.name = name
            if address:
                platform.address = address
            platform.save()
            return Response(status=200)
        except:
            return self.handler500
        
    def destroy(self, request, *args, **kwargs):
        platform = self.get_platform_entity()

        try:
            platform.delete()
            return Response(status=200)
        except:
            return self.handler500
    