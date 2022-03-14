from django.contrib import admin

# Register your models here.

#importing ClientProfile class from Model
from .models import ClientProfileModel  
admin.site.register((ClientProfileModel))