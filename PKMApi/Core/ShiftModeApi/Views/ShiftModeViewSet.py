from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, ValidationError

from ..Serializers.ShiftModeSerializer import ShiftModeApiSerializer

from Core.models.ShiftMode import ShiftMode

from Core.models.Company import Company

class ShiftModeApiViewSet(ModelViewSet):
    
    serializer_class = ShiftModeApiSerializer

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_company(self):
        company_code = self.kwargs.get('company_code')
        try:
            return Company.objects.get(code=company_code)
        except:
            raise NotFound({'error': 'Такой компании не найдено'})
    
    def get_shift_mode_list(self):
        shift_modes = ShiftMode.objects.filter(company__code=self.get_company().code)
        if shift_modes.exists():
            return shift_modes
        else:
            raise NotFound({'error': 'Режимов сменности не найдено'})

    def code_validation(self, code, company):
        if ShiftMode.objects.filter(code=code, company=company).exists():
            raise ValidationError({'error': 'Такой код режима сменности уже существует'})
    
    def get_shift_mode_entity(self):
        try:
            return ShiftMode.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'error': 'Такого режима сменности не найдено'})

    def create(self, request, *args, **kwargs):
        company = self.get_company()

        data = request.data
        data['company'] = company.pk

        self.code_validation(code=request.data.get('code'), company=company)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        shift_modes = self.get_shift_mode_list()
        try:
            serializer = self.get_serializer(shift_modes, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
        
    def retrieve(self, request, *args, **kwargs):
        shift_mode = self.get_shift_mode_entity()
        try:
            serializer = self.get_serializer(shift_mode)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
    
    def update(self, request, *args, **kwargs):
        shift_mode = self.get_shift_mode_entity()

        company = self.get_company()
        self.code_validation(code=request.data.get('code'), company=company)

        try:
            serializer = self.get_serializer(shift_mode, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.handler200
        except:
            return self.handler500

    def destroy(self, request, *args, **kwargs):
        shift_mode = self.get_shift_mode_entity()
        try:
            shift_mode.delete()
            return self.handler200
        except:
            return self.handler500
        