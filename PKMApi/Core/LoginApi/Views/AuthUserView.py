import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed

from ..Rules import rule_window_kadrovik, rule_winodw_planovik

from Core.models.User import User


class AuthUserApiView(APIView):

    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def post(self, request, company_code):
        
        login = request.data.get('login')
        password = request.data.get('password')

        try:
            user = User.objects.get(company__code=company_code, login=login, password=password)
        except:
            raise NotFound({'error': 'Такой пользователь не найден, проверьте введённые данные'})
        
        if not user.is_activated:
            raise NotFound({'error': 'Пользователь не активирован, обратитесь к кадровику или администратору'})

        if user.token:
            raise AuthenticationFailed({'error': 'Вход невозможен: активный сеанс уже существует'})
        
        new_token = str(uuid.uuid4())
        user.token = new_token
        user.save()

        if user.role_1.name == 'Кадровик':
            rule_window_kadrovik.update({'token': user.token})
            return Response(rule_window_kadrovik, status=200)
        elif user.role_1.name == 'Плановик':
            rule_winodw_planovik.update({'token': user.token})
            return Response(rule_winodw_planovik, status=200)
    