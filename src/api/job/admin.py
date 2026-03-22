from django.contrib import admin

from core.admin import BaseAdmin
from job.models import Skill , JobOpening , JobEnrollment

# Register your models here.
@admin.register(Skill)
class SkillAdmin(
    BaseAdmin
):

    list_display = ["name" , "slug"]
    prepopulated_fields = {"slug" : ["name"]}

@admin.register(JobOpening)
class JobOpeningAdmin(
    BaseAdmin
):
    list_display = ['title' , 'created_at']
    
@admin.register(JobEnrollment)
class JobEnrollmentAdmin(
    BaseAdmin
):
    
    list_display = ['job' , 'user']