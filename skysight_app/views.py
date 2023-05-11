from django.shortcuts import render, redirect
from .api import get_flight_data, get_weather_data
from .forms import FlightSearchForm, CitySearchForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404

from .models import *

def home(request):
    return render(request, 'home.html')


@login_required
def flight_view(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            flight_number = form.cleaned_data['flight_number']
            data = get_flight_data(flight_number)
            print(data)
            flight_data = None
            if data.get('data'):
                flight_data = data['data'][0]
            return render(request, 'flight/index.html', {'flight': flight_data})
    else:
        form = FlightSearchForm()
    return render(request, 'flight/flight_search.html', {'form': form})

@login_required
def weather_view(request):
    if request.method == 'POST':
        form = CitySearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
            weather = WeatherData(
                user=request.user,
                city=city,
                temperature=weather_data['current']['temp_c'],
                condition=weather_data['current']['condition']['text'],
            )
            all_weather = WeatherData.objects.filter(user=request.user)
            return render(request, 'weather/weather_search.html', {'form': form, 'weather': weather, 'all_weather': all_weather})
    else:
        form = CitySearchForm()
        all_weather = WeatherData.objects.filter(user=request.user)
    return render(request, 'weather/weather_search.html', {'form': form, 'all_weather': all_weather})

@login_required
def delete_weather_view(request, weather_id):
    weather = get_object_or_404(WeatherData, id=weather_id)
    if request.method == 'POST':
        weather.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(['POST'])  

@login_required
def update_weather_view(request, weather_id):
    weather = get_object_or_404(WeatherData, id=weather_id)
    if request.method == 'POST':
        form = CitySearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
            weather.city = city
            weather.temperature = weather_data['current']['temp_c']
            weather.condition = weather_data['current']['condition']['text']
            weather.save()
            return redirect('weather')
    else:
        form = CitySearchForm(initial={'city': weather.city})
    return render(request, 'weather/weather_update.html', {'form': form, 'weather': weather})

@login_required
def save_weather_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        temperature = request.POST.get('temperature')
        condition = request.POST.get('condition')
        weather = WeatherData.objects.create(
            user=request.user,
            city=city,
            temperature=temperature,
            condition=condition,
        )
        return redirect('index')
    else:
        return HttpResponseNotAllowed(['POST'])

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
