from account.models import Profile
from account.permissions import IsAuthenticated, IsProfileOwner
from account.serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
    RegisterUserSerializer,
    UserEnrollmentsSerializer,
)
from core.utils import get_access_refresh_token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from job.models import JobEnrollment
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
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
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission = self.permission_per_method.get(self.request.method)
        if permission:
            return [permission()]

        return super().get_permissions()

    def get_serializer_class(self):
        serializers = {
            "PUT" : ProfileUpdateSerializer,
            "PATCH" : ProfileUpdateSerializer
        }
        return serializers.get(self.request.method, super().get_serializer_class())

    def get_object(self):
        username = self.kwargs.get("username")
        return get_object_or_404(Profile , user__username = username)

class UserEnrollmentsView(
    ListAPIView
):

    permission_classes = [IsAuthenticated]
    serializer_class = UserEnrollmentsSerializer

    def get_queryset(self):
        return JobEnrollment.objects.filter(user = self.request.user)
