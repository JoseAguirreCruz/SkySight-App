from django import forms

class FlightSearchForm(forms.Form):
    flight_number = forms.CharField(label='Flight Number', max_length=100)

class CitySearchForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)