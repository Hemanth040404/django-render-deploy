import requests
from django.shortcuts import render

def index(request):
    weather_data = {}
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = '9ed8895053d4c2425495d43b362606f7'  # ✅ confirmed working
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found! Please enter a valid city name.'}
    return render(request, 'weather_app/index.html', {'weather': weather_data})