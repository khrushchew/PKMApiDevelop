from drf_yasg import openapi

ACCESS_TOKEN_PARAM = openapi.Parameter(
            'Authorization',
            openapi.IN_HEADER,
            description='Токен доступа',
            type=openapi.TYPE_STRING,
            required=True,
            default='JWT {token}'
        )

MACHINE_STYLE_PARAM = openapi.Parameter(
            'style',
            openapi.IN_QUERY,
            description='Вид оборудования',
            type=openapi.TYPE_INTEGER,
            required=False,
)
