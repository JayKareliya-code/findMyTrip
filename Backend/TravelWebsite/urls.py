"""
URL configuration for TravelWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .findmytrip import views
from rest_framework import routers
from django.contrib.auth.views import LoginView

router = routers.DefaultRouter()
router.register(r'hotels', views.HotelViewSet)
router.register(r'flights', views.FlightViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'packages', views.PackageViewSet)
router.register(r'bookings', views.BookingViewSet, basename='booking')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]