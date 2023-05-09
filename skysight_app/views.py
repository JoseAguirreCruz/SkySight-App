from django.shortcuts import render
from .api import get_flight_data
from .forms import FlightSearchForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

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




