from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.


def home_view(request, *args, **kwargs):
    my_context = {
        'name': 'cool',
        'teams': ['LAL', 'LAC', 'GSW', 'SAS']
    }
    return render(request, "home.html", my_context)


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact</h1>')
