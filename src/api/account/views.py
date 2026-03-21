from account.models import Profile
from account.permissions import IsProfileOwner
from account.serializers import ProfileSerializer, RegisterUserSerializer
from core.utils import get_access_refresh_token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

USER = get_user_model()

# Create your views here.
class RegisterUserView(
    CreateAPIView
):

    queryset = USER.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        tokens = get_access_refresh_token(user)
        return Response(
            tokens,
            status=status.HTTP_201_CREATED
        )

class ProfileDetailView(
    RetrieveUpdateAPIView
):
    serializer_class = ProfileSerializer
    permission_per_method = {
        "PUT" : IsProfileOwner
    }

    def get_permissions(self):
        permission = self.permission_per_method.get(self.request.method)
        if permission:
            return [permission()]

        return super().get_permissions()

    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(Profile , user__username = username)
