import requests
from django.shortcuts import render
from .models import City


def index(request):
    appid = 'a8a709791f27a328cc9693ae6f0ab678'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(res)
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities}

    return render(request, 'weather/index.html', context)  #by default, it starts to looking for in /templates

