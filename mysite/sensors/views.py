from .models import TemHem
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request):
    temhum_list = TemHem.objects.order_by('-data_time')[:10]

    return render(request, 'sensors/index.html', {"temhum_list": temhum_list})


def update(request):
    # receive data from sensors
    # common url looks like: /sensors/update/?tem=12.3&hum=45.6

    tem = request.GET['tem']
    hum = request.GET['hum']

    a = TemHem()
    a.temperature = tem
    a.humidity = hum
    a.save()

    return HttpResponse("Yep, your temperature is " + tem + ", and Humidity is %s!" % hum)
