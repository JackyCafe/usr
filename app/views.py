from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets

from app.forms import ReadingForm
from app.models import Reading
from app.serializers import ReadingSerializers


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
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializers