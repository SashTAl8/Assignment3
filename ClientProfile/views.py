from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homeview(request, *args, **kwargs):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def clienthome(request, *args, **kwargs):
    #return HttpResponse("<h1>Profile Page</h1>")
    return render(request, "clientmode.html", {})

def profile(request, *args, **kwargs):
    #return HttpResponse("<h1>Profile Page</h1>")
    return render(request, "profile.html", {})

def fuelQuote(request, *args, **kwargs):
    #return HttpResponse("<h1>Fuel Quote</h1>")
    return render(request, "fuelquote.html", {})


def history(request, *args, **kwargs):
    #return HttpResponse("<h1>Fuel Quote History</h1>")
    return render(request, "history.html", {})


def login(request, *args, **kwargs):
    #return HttpResponse("<h1>Login Page</h1>")
    return render(request, "login.html", {})


def register(request, *args, **kwargs):
    return render(request, "register.html", {})

def guestpage(request, *args, **kwargs):
    return render(request, "guessmode.html", {})
