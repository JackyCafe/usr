from rest_framework import serializers
from rest_framework.routers import DefaultRouter

from app import views
from app.models import Reading

class ReadingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = '__all__'
