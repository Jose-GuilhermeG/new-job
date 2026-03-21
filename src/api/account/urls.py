from account import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path(
        'account/register/',
        views.RegisterUserView.as_view(),
        name="register"
    ),
    path(
        'users/<str:username>/profile/',
        views.ProfileDetailView.as_view(),
        name="profile"
    )
]

urlpatterns += [
    path(
        'account/login/',
        TokenObtainPairView.as_view(),
        name='login',
    ),
    path(
        'account/logout/',
        TokenBlacklistView.as_view(),
        name='logout',
    ),
    path(
        'account/token/verify/',
        TokenVerifyView.as_view(),
        name="token-verify",
    ),
    path(
        'account/token/refresh/',
        TokenRefreshView.as_view(),
        name="token-refresh",
    )
]
