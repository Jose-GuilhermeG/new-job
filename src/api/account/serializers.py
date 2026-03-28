from account.models import Profile
from django.contrib.auth import get_user_model
from job.models import JobEnrollment, Skill
from job.serializers import JobOpeningListSerializer, SkillSerializer
from rest_framework import serializers

USER = get_user_model()

class RegisterUserSerializer(
    serializers.ModelSerializer
):
    email = serializers.EmailField(allow_blank=False)

    class Meta:
        model = USER
        fields = ["username" , "email" , "password"]


    def create(self, validated_data : dict):
        return USER.objects.create_user(**validated_data)

class ProfileSerializer(
    serializers.ModelSerializer
):

    skills = SkillSerializer(many=True , read_only = True)

    class Meta:
        model = Profile
        exclude = ['user',"created_by","updated_by","is_active"]
        read_only_fields = ["created_at","updated_at",]

class ProfileUpdateSerializer(
    ProfileSerializer
):
    skills = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Skill.objects.all(),
        write_only=True
    )

class UserEnrollmentsSerializer(
    serializers.ModelSerializer
):
    job = JobOpeningListSerializer()
    class Meta:
        model = JobEnrollment
        fields = ["id","job"]
