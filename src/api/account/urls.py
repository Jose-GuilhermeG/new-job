from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView , TokenObtainPairView , TokenRefreshView , TokenVerifyView
from account import views

urlpatterns = [
    path(
        'register/',
        views.RegisterUserView.as_view(),
        name="register"
    )
]

urlpatterns += [
    path(
        'login/',
        TokenObtainPairView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        TokenBlacklistView.as_view(),
        name='logout',
    ),
    path(
        'token/verify/',
        TokenVerifyView.as_view(),
        name="token-verify",
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name="token-refresh",
    )
]