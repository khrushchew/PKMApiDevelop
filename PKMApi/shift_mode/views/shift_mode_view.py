from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated


from shift_mode.serializers.shift_mode_create_serializer import ShiftModeCreateSerializer
from shift_mode.serializers.shift_mode_list_serializer import ShiftModeListSerializer

from Core.models.ShiftMode import ShiftMode


class ShiftModeView(ViewSet):

    permission_classes = [IsAuthenticated]

    handler200 = Response(status=200)
    handler201 = Response({'detail': 'Ражим сменности успешно создан'}, status=201)
    handler500 = Response({'detail': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def get_shift_mode_list(self):
        shift_modes = ShiftMode.objects.filter(company=self.request.user.company)
        if shift_modes.exists():
            return shift_modes
        else:
            raise NotFound({'detail': 'Режимов сменности не найдено'})

    def get_shift_mode_entity(self):
        try:
            return ShiftMode.objects.get(pk=self.kwargs.get('pk'))
        except:
            raise NotFound({'detail': 'Такого режима сменности не найдено'})

    def create(self, request, *args, **kwargs):
        data = request.data
        data['company'] = request.user.company.pk

        serializer = ShiftModeCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
            return self.handler201
        except:
            return self.handler500

    def list(self, request, *args, **kwargs):
        shift_modes = self.get_shift_mode_list()
        try:
            serializer = ShiftModeListSerializer(shift_modes, many=True)
            return Response(serializer.data, status=200)
        except:
            return self.handler500
        
    # def retrieve(self, request, *args, **kwargs):
    #     shift_mode = self.get_shift_mode_entity()
    #     try:
    #         serializer = self.get_serializer(shift_mode)
    #         return Response(serializer.data, status=200)
    #     except:
    #         return self.handler500
    
    def update(self, request, *args, **kwargs):
        shift_mode = self.get_shift_mode_entity()

        serializer = ShiftModeCreateSerializer(shift_mode, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
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
        