import requests
from django.shortcuts import render


def index(request):
    appid = 'a8a709791f27a328cc9693ae6f0ab678'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'London'

    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]['icon']
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)  #by default, it starts to looking for in /templates

