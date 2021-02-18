from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Login")

def register(response):
        return render(response, "home/register.html", {}) #might be mysite instead of home