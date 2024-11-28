from drf_yasg import openapi

ACCESS_TOKEN_PARAM = openapi.Parameter(
            'access_token',
            openapi.IN_HEADER,
            description='Токен доступа',
            type=openapi.TYPE_STRING,
            required=True,
            default='JWT {token}'
        )