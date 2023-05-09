from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('flight/index/', views.flight_view, name='index'),
  path('weather/index/', views.weather_view, name='weather'),
]