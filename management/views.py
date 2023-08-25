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

def addpage(request):
    if request.method == 'POST':
        print(request.POST['name'],
            request.POST['group'],
            request.POST['capacity'])
        models.management.objects.create(
            name = request.POST['name'],
            group = request.POST['group'],
            capacity = request.POST['capacity']
            )
        return redirect(reverse ('management:homepage'))
    return render(request,'add.html')
