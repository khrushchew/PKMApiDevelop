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
    
    def retrieve(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            serializer = SubdivisionRetrieveSerializer(subdivision)
            return Response(serializer.data, status=200)
        except:
            return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def update(self, request, *args, **kwargs):
        
        subdivision = self.get_subdivision_entity()

        self.check_name()

        serializer = SubdivisionUpdateSerializer(subdivision, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return Response(status=200)
        except:
            return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        
    def destroy(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            subdivision.delete()
            return Response(status=200)
        except:
            return Response({'detali': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        