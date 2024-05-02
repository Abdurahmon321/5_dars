from django.shortcuts import render

from .models import Home


# Create your views here.


def index(request):
    return render(request, "app/index.html")


def all_homes(request):
    return render(request, 'all_homes/all_homes.html')


def home_detail(request, id):
    home = Home.objects.get(id=id)
    return render(request, "home_detail/home_detail.html", {"home": home})
