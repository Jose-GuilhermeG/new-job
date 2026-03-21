from django.utils.text import slugify
from job.models import Skill
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
