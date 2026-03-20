from django.contrib.auth import get_user_model
from rest_framework import serializers

USER = get_user_model()

class RegisterUserSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = USER
        fields = ["username" , "email" , "password"]

    def create(self, validated_data : dict):
        return USER.objects.create_user(**validated_data)
