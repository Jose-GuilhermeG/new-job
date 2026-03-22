from django.utils.text import slugify
from rest_framework import serializers
from django.utils.timezone import datetime , make_naive , timedelta

from job.models import Skill , JobOpening

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