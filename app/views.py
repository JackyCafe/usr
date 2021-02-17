from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.forms import ReadingForm
from app.models import Reading, Blog, myActivity, Activity
from app.serializers import ReadingSerializers, BlogSerializers, UserSerializers, myActivitySerializers, \
    ActivitySerializers


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def index(request):
    return HttpResponse('媽~我在這裡')


def readings(request):
    readings = Reading.objects.all()
    context = {'readings':readings}
    return  render(request,'app/readings.html',context)


def uploadReading(request):
    if request.method == 'POST':
        form = ReadingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:readings')
    else:
        form = ReadingForm()
    return render(request, 'app/upload.html', {'form' : form})



class ReadingViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializers
    # http_method_names = ("post", "patch")
    authentication_classes = (JWTAuthentication,)


class BlogViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

    queryset = Blog.objects.all()
    serializer_class =  BlogSerializers


class ActivitySet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    queryset =  Activity.objects.all()
    serializer_class = ActivitySerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class myActivitySet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
    queryset = myActivity.objects.all()
    serializer_class = myActivitySerializers