from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from Core.models.User import User

class LogoutUserApiView(APIView):

    def post(self, request, company_code):

        login = request.data.get('login')
        password = request.data.get('password')

        try:
            user = User.objects.get(company__code=company_code, login=login, password=password)
        except:
            raise NotFound({'error': 'Такой пользователь не найден, проверьте введённые данные'})
        
        user.token = None
        user.save()

        return Response({'message': 'Вы успешно вышли из системы'}, status=200)
