from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LogoutView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        
        user.session = False
        user.save()

        return Response({'detail': 'Вы успешно вышли из системы!'}, status=200)
