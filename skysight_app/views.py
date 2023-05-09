from django.shortcuts import render, redirect
from .api import get_flight_data, get_shipment_data, get_weather_data
from .forms import FlightSearchForm, CitySearchForm, ShipmentSearchForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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
            return render(request, 'weather/index.html', {'weather': weather_data})
    else:
        form = CitySearchForm()
    return render(request, 'weather/weather_search.html', {'form': form})

@login_required
def shipment_search_view(request):
    form = ShipmentSearchForm(request.GET or None)
    if form.is_valid():
        tracking_number = form.cleaned_data.get('tracking_number')
        if tracking_number:
            data = get_shipment_data(tracking_number)
            return render(request, 'shipment/index.html', {'data': data})
    return render(request, 'shipment/shipment_search.html', {'form': form})

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
