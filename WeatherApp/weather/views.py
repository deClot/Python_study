from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')  #by default, it starts to looking for in /templates 
