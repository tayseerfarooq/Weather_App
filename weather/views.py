# weather/views.py

import requests
from django.shortcuts import render
from .forms import CityForm

def index(request):
    weather = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = 'e48a4e53c05eeda678c905b9c328cc91'
            url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'
            response = requests.get(url)
            data = response.json()
            
            if 'current' in data:
                weather = {
                    'city': data['location']['name'],
                    'temperature': data['current']['temperature'],
                    'description': data['current']['weather_descriptions'][0],
                    'icon': data['current']['weather_icons'][0]
                }
            else:
                weather = {'error': 'Could not retrieve weather data for this location.'}
    else:
        form = CityForm()

    return render(request, 'weather/index.html', {'form': form, 'weather': weather})
