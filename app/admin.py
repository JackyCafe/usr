from django.contrib import admin

# Register your models here.
from app.models import UserProfile, Reading


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['title','category','created','content','user']
