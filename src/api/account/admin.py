from account.models import Profile, ProfileSkill
from core.admin import BaseAdmin
from django.contrib import admin


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ['user' , "name"]

@admin.register(ProfileSkill)
class ProfileSkillAdmin(admin.ModelAdmin):
    pass
