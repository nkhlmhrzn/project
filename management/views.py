from . import models

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

def homepage(request):
    management = models.management.objects.all()
    return render(request,'home.html',{
        "management":management
    })

def availablepage(request):
    management = models.management.objects.all()
    return render(request,'available.html',{
        "management":management
    })
