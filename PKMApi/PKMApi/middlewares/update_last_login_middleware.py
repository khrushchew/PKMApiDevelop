from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

class UpdateLastLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_auth = JWTAuthentication()
        if request.headers.get('Authorization'):
            try:
                user = jwt_auth.authenticate(request)[0]
                user.last_login = timezone.now()
                user.save()
            except AuthenticationFailed:
                pass

        return self.get_response(request)