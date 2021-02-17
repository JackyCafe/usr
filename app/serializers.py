from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.routers import DefaultRouter

from app import views
from app.models import Reading, Blog, myActivity,Activity


class ReadingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class myActivitySerializers(serializers.ModelSerializer):

    class Meta:
        model = myActivity
        fields = '__all__'


class ActivitySerializers(serializers.ModelSerializer):
    activity = myActivitySerializers(many=True,source='title')
    class Meta:
        model = Activity
        fields = '__all__'







class UserSerializers(serializers.ModelSerializer):
    blog = BlogSerializers(many=True,source='user')
    myActivity = myActivitySerializers(many=True,source='my_activity')

    class Meta:
        model = User
        fields = '__all__'


