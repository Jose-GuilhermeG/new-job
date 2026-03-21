from datetime import timedelta

from configs.settings.general import DEBUG, env

CORS_ALLOW_ALL_ORIGINS = DEBUG

CORS_ALLOWED_ORIGINS = env.list("CORS_ORIGINS" , default=[])

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=25),
    'REFRESH_TOKEN_LIFETIME' : timedelta(days=5),
    'SIGNING_KEY' : env('JWT_SIGNING_KEY'),
    'TOKEN_OBTAIN_SERIALIZER' : 'account.serializers.LoginSerializer',
    'UPDATE_LAST_LOGIN' : True
}


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '100/min'
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS' : ['django_filters.rest_framework.backends.DjangoFilterBackend']

}
