from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, AuthenticationFailed
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from Core.models.User import User
from ..Serializers.AuthUserSerializer import AuthUserApiSerializer


class AuthUserApiView(APIView):
    handler200 = Response(status=200)
    handler500 = Response({'error': 'Что-то пошло не так, повторите попытку позже'}, status=500)

    def post(self, request, company_code):

        data = request.data

        username = data.get('username', None)

        password = data.get('password', None)

        if username is None or password is None:

            return Response({'error': 'Нужен и логин, и пароль'}, status=400)

        user = authenticate(username=username, password=password)

        if user is None:

            return Response({'error': 'Неверные данные'}, status=401)

        refresh = RefreshToken.for_user(user)

        refresh.payload.update({
            'user_id': user.id,
            'username': user.username
        })


        return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user.username,
                'groups': [group.name for group in user.groups.all()],
            }, status=200)

