"""JWTProject URL Configuration

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
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app.views import ReadingViewSet, BlogViewSet, UserViewSet, HelloView, myActivitySet, ActivitySet, registraion_view, \
    score

router = DefaultRouter()
router.register(r'user',UserViewSet)
router.register(r'reading',ReadingViewSet)
router.register(r'blog',BlogViewSet)
router.register(r'myActivity',myActivitySet)
router.register(r'Activity',ActivitySet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
    path('register',registraion_view,name='registraion_view'),
    path('score/',score,name='score'),
    url(r'api/', include(router.urls)),
]
