"""usr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from app import views


app_name = 'app'
urlpatterns = [
    # path('',views.index,name='index'),
    path('reading/upload/', views.uploadReading, name='uploadReading'),
    path('reading/', views.readings, name='readings'),

]
