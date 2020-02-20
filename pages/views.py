from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello world</h1>')


def contact_view(request, *args, **kwargs):
    return HttpResponse('<h1>Contact</h1>')
