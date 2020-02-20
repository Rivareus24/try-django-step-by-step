from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact</h1>')
