from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from ..Serializers.SubdivisionSerializer import SubdivisionApiSerializer

from Core.models.Subdivision import Subdivision
from Core.models.Company import Company


class SubdivisionApiViewSet(ModelViewSet):
    serializer_class = SubdivisionApiSerializer
    queryset = Subdivision.objects.all()

    def get_subdivision_list(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Subdivision.objects.filter(company__code=company_code)
        except:
            raise NotFound({'error': 'Подразделений не найдено'})
    
    def get_subdivision_entity(self):
        pk = self.kwargs.get('pk')
        try:
            return Subdivision.objects.get(pk=pk)
        except:
            raise NotFound({'error': 'Такого подразделения не найдено'})

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})

    
    def create(self, request, *args, **kwargs):
        name = request.data.get('name')

        company = self.get_company()

        if Subdivision.objects.filter(name=name, company__code=company.code).exists():
            return Response({'error': 'Роль с таким названием уже существует'}, status=409)

        try:    
            Subdivision.objects.create(name=name, company=company)
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def list(self, request, *args, **kwargs):
        subdivisions = self.get_subdivision_list()

        try:
            serializer = self.get_serializer(subdivisions, many=True)

            for i in range(1, len(serializer.data) + 1):
                serializer.data[i - 1].setdefault("id", i)

            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
    
    def retrieve(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            serializer = self.get_serializer(subdivision)
            return Response(serializer.data, status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def update(self, request, *args, **kwargs):
        name = request.data.get('name')

        subdivision = self.get_subdivision_entity()
       
        if Subdivision.objects.filter(name=name, company__code=subdivision.company.code).exists():
            return Response({'error': 'Роль с таким названием уже существует'}, status=409)

        try:
            subdivision.name = name
            subdivision.save()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        

    def destroy(self, request, *args, **kwargs):
        subdivision = self.get_subdivision_entity()

        try:
            subdivision.delete()
            return Response(status=200)
        except:
            return Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)
        