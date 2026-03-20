from rest_framework_simplejwt.tokens import RefreshToken


def get_access_refresh_token(user):
    refresh_token = RefreshToken.for_user(user)
    return {
        "access": str(refresh_token.access_token),
        "refresh": str(refresh_token)
    }
