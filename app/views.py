from django.shortcuts import render
from .utils import get_weather_data


# Create your views here.

def home(request):
    get_data = None
    lon = ""
    lat = ""
    if request.method == 'POST':
        lon = request.POST.get('lon')
        lat = request.POST.get('lat')
        get_data = get_weather_data(lat, lon)
    return render(request, 'index.html', {'weather_data': get_data, 'lon': lon, 'lat': lat})
