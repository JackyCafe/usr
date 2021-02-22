import django_filters
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.forms import ReadingForm
from app.models import Reading, Blog, myActivity, Activity
from app.serializers import ReadingSerializers, BlogSerializers, UserSerializers, myActivitySerializers, \
    ActivitySerializers, RegisterationSerializers, ScoreSerializers


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


@api_view(['POST',])
def registraion_view(request):
    if request.method == 'POST':
        serializer = RegisterationSerializers(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully "
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return  Response(data)


@api_view(['GET'])
def score(request):
    if request.method == 'GET':
        queryset = myActivity.objects.values('user').annotate(score=Sum('point'))
        # serializer = ScoreSerializers()
        filterset_fields = ('user',)
        filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
        return HttpResponse(queryset, status=status.HTTP_200_OK)
