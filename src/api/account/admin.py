from django.contrib import admin

from core.admin import BaseAdmin
from account.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ['user' , "name"]