from django.utils.text import slugify
from django.utils.timezone import datetime, make_naive
from django.utils.translation import gettext_lazy as _
from job.models import JobEnrollment, JobOpening, Skill
from rest_framework import serializers


class SkillSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Skill
        fields = ["id" , "name" , "slug"]
        read_only_fields = ["id" , "slug"]

    def save(self, **kwargs):
        slug = slugify(self.validated_data.get("name"))
        kwargs["slug"] = slug
        return super().save(**kwargs)

class JobOpeningListSerializer(
    serializers.ModelSerializer
):
    current_time = serializers.SerializerMethodField()

    class Meta:
        model = JobOpening
        fields = ["id" ,"title" , "type" , "location" , "current_time"]

    def get_current_time(self , obj) :
        now = datetime.now()
        current = (now - make_naive(obj.start_at)).days
        return current

class JobOpeningCreateUpdateSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = JobOpening
        exclude = ["id" ,"is_active" , "created_at" , "created_by" , "updated_at" , "updated_by"]

class JobOpeningDetailSerializer(
    serializers.ModelSerializer
):
    skills = SkillSerializer(many = True)

    class Meta:
        model = JobOpening
        exclude = ["id" ,"is_active" , "created_at" , "created_by" , "updated_at" , "updated_by"]

class JobEnrollmentSerializer(
    serializers.ModelSerializer
):
    user = serializers.CharField(source="user.profile.name",read_only=True)
    leveraging_skills = serializers.SerializerMethodField()

    class Meta:
        model = JobEnrollment
        fields = ["id" , "user" , "contact_email" , "curriculum" , "leveraging_skills"]

    def get_leveraging_skills(self , obj) -> float :
        user_skills = obj.user.profile.skills.values_list("name", flat=True)
        leveraing = round((obj.job.skills.filter(name__in = user_skills ).count() * 100) / obj.job.skills.count(),2)
        return leveraing

    @staticmethod
    def check_enrollment(user , email , job) -> None:
        if(job.enrollments.filter(user = user).exists()):
            raise serializers.ValidationError(_("The user is already registered."))

        if(job.enrollments.filter(contact_email = email).exists()):
            raise serializers.ValidationError(_("The email is already registered."))

    def create(self, validated_data):
        user = validated_data.get("user")
        email = validated_data.get("contact_email")
        job = validated_data.get("job")

        self.check_enrollment(user , email , job)

        return super().create(validated_data)
