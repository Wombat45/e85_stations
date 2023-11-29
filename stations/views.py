from django.shortcuts import render
from .forms import StationForm
from django.core.paginator import Paginator
import requests
import os

def index(request):
    form = StationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            zip_code = form.cleaned_data['zip_code']
            miles = form.cleaned_data['miles']
            url = "https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json"
            response = requests.get(url, params={"format": "json", "api_key": os.environ["NREL_API_KEY"], "location": zip_code, "fuel_type": "E85", "radius": miles, "status": "E"})
            stations = response.json()['fuel_stations']
            # Extract more information about each station
            stations_info = []
            for station in stations:
                info = {
                    'name': station['station_name'],
                    'distance': station['distance'],
                    'street_address': station['street_address'],
                    'city': station['city'],
                    'state': station['state'],
                }
                stations_info.append(info)
            request.session['stations_info'] = stations_info  # Store the stations info in the session

    elif 'stations_info' in request.session:
        stations_info = request.session['stations_info']  # Retrieve the stations info from the session
    else:
        stations_info = []

    paginator = Paginator(stations_info, 10)  # Show 10 stations per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'form': form, 'page_obj': page_obj})