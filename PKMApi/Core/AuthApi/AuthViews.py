from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .Rules import rule_window_kadrovik

from .AuthSerializers import AuthSerializer
from ..models.User import User


class AuthApiView(CreateAPIView):
    serializer_class = AuthSerializer

    def post(self, request):
        company_code = request.data.get('company_code')
        login = request.data.get('login')
        password = request.data.get('password')
        try:
            user = User.objects.get(login=login)
            if password == user.password:
                if company_code == user.subdivision.area.department.platform.company.code:
                    if user.is_activated is True:
                        serializer = AuthSerializer(user)
                        response_data = serializer.data
                        response_data['role'] = user.role.name
                        if response_data['role'] == 'Кадровик':
                            response_data.update({'windows': rule_window_kadrovik})
                        return Response(response_data, status=200)
                    else:
                        return Response({'error': 'Аккаунт не активен'}, status=423)
                else:
                    return Response({'error': 'Проверьте компанию'}, status=400)
            else:
                return Response({'error': 'Неверный пароль'}, status=400)
        except:
            return Response({'error': 'Пользователя не существует'}, status=404)

