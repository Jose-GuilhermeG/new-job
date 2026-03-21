from core.admin import BaseAdmin
from django.contrib import admin
from job.models import Skill


# Register your models here.
@admin.register(Skill)
class SkillAdmin(
    BaseAdmin
):

    list_display = ["name" , "slug"]
