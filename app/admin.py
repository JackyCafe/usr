from django.contrib import admin

# Register your models here.
from app.models import UserProfile, Reading,Activity,myActivity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]


@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['title','category','created','content','user']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Activity._meta.fields]

@admin.register(myActivity)
class myActivityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in myActivity._meta.fields]