from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..Serializers.LogoutUserSerializer import LogoutUserApiSerializer

from Core.models.User import User

from rest_framework_simplejwt.tokens import RefreshToken


class LogoutUserApiView(APIView):

    
