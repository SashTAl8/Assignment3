from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, "home.html", {})

def profile_view(*args, **kwargs):
    return HttpResponse("<h1>Profile Page</h1>")

def fuelQuote(*args, **kwargs):
    return HttpResponse("<h1>Fuel Quote</h1>")

def fuelQuoteHistory(*args, **kwargs):
    return HttpResponse("<h1>Fuel Quote History</h1>")

def login(*args, **kwargs):
    return HttpResponse("<h1>Login Page</h1>")

def register(*args, **kwargs):
    return HttpResponse("<h1>Register Page</h1>")