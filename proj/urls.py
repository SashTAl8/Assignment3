"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from ClientProfile.views import homeview,guestpage, clienthome, profile, fuelQuote, history, login, register
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('clienthome/', views.clienthome),
    path('fuelQuote/', views.fuelQuote),
    path('guestpage/', views.guestpage),
    path('history/', views.history),
    path('login/', views.login),
    path('profile/', views.profile),
    path('register/', views.register),
    path('admin/', admin.site.urls),
    
]
