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
    # activity = myActivitySerializers(many=True)
    class Meta:
        model = Activity
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    blog = BlogSerializers(many=True,source='user')
    myActivity = myActivitySerializers(many=True,source='my_activity')

    class Meta:
        model = User
        fields = '__all__'


class RegisterationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ('username','password','password2','email')
        extra_kwargs = {'password':{'write_only':True}}

    def save(self):
        print(self.validated_data)
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
