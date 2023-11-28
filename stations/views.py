from django.shortcuts import render
from .forms import StationForm
import requests
import os

def index(request):
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            zip_code = form.cleaned_data['zip_code']
            miles = form.cleaned_data['miles']
            url = "https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json"
            response = requests.get(url, params={"format": "json", "api_key": os.environ["NREL_API_KEY"], "location": zip_code, "fuel_type": "E85", "radius": miles, "status": "E"})
            stations = response.json()['fuel_stations']
            return render(request, 'index.html', {'form': form, 'stations': stations})
    else:
        form = StationForm()
    return render(request, 'index.html', {'form': form})