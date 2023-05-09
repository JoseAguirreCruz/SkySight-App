from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flight/index/', views.flight_view, name='index'),
    path('weather/index/', views.weather_view, name='weather'),
    path('shipment/index', views.shipment_search_view, name='shipment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
