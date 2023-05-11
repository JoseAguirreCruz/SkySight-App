from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flight/index/', views.flight_view, name='index'),
    path('weather/index/', views.weather_view, name='weather'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('weather/update/<int:weather_id>/', views.update_weather_view, name='update_weather_data'),
    path('weather/delete/<int:weather_id>/', views.delete_weather_view, name='delete_weather_data'),    
    path('weather/save/', views.save_weather_view, name='save_weather'),
]
