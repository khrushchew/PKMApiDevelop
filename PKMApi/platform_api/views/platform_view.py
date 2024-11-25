from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.viewsets import ViewSet

from ..serializers.platform_create_serializer import PlatformCreateSerializer
from ..serializers.platform_list_serializer import PlatformListSerializer
from ..serializers.platform_update_serializer import PlatformUpdateSerializer

from Core.models.Platform import Platform

from rest_framework.permissions import IsAuthenticated


class PlatformView(ViewSet):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler201 = Response(status=201)
    handler204 = Response(status=204)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_platform_list(self):
        try:
            return Platform.objects.filter(company=self.request.user.company).order_by('indent')
        except:
            raise NotFound({'detail': 'Площадок не найдено'})
    
    def get_platform_entity(self):
        try:
            return Platform.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'detail': 'Такой площадки не найдено'})

    def check_name(self):
        if Platform.objects.filter(name=self.request.data.get('name'), company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Площадка с таким названием уже существует'})
    
    def check_indent(self):
        if Platform.objects.filter(indent=self.request.data.get('indent'), company=self.request.user.company).exists():
            raise ValidationError({'detail': 'Площадка с таким идентификатором уже существует'})

    def create(self, request, *args, **kwargs):

        data = request.data

        data["company"] = request.user.company.pk

        self.check_name()
        self.check_indent()

        serializer = PlatformCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return self.handler201
        except:
            return self.handler500
    
    def list(self, request, *args, **kwargs):

        platforms = self.get_platform_list()

        try:
            serializer = PlatformListSerializer(platforms, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500

    def retrieve(self, request,  *args, **kwargs):
        platform = self.get_platform_entity()
        try:
            serializer = PlatformCreateSerializer(platform)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
        
    def update(self, request, *args, **kwargs):

        data = request.data

        self.check_name()
        self.check_indent()

        platform = self.get_platform_entity()

        try:
            serializer = PlatformUpdateSerializer(platform, data=data, partial=True)
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
    