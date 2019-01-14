from django.shortcuts import render
from .models import Carssection
from django.http import HttpResponse

def car_list(request):
    cars = Carssection.objects.all().order_by('date')
    return render(request,"carssection/cars.html",{'cars':cars}) #render and will output the data in ( whaterver>cars:cars<above things)


def car_detail(request, slug):
    #return HttpResponse(slug)
    car = Carssection.objects.get(slug=slug)
    return render(request, "carssection/car_detail.html", {'car':car})
