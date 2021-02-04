from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.routers import DefaultRouter

from app import views
from app.models import Reading, Blog


class ReadingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    blog = BlogSerializers(many=True,source='user')

    class Meta:
        model = User
        fields = '__all__'

