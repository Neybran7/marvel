#import requests
import json
from django.shortcuts import redirect, render
from .models import *
from .forms import UserREgisterForm
from django.contrib import messages


def inicio(request):
    #return render(request, 'social/feed.html', {'nombre':nombre})
    nombre = "Neybran"
    return render(request, 'social/feed.html' , {'nombre':nombre})

def profile(request):
    #aca ya esta logeado ? si
    marvel_datos = "api de marvel"
    return render(request, 'social/profile.html' , {'marvel_api':marvel_datos})

def register(request):
    #aca no
    if request.method=='POST':
        form=UserREgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form=UserREgisterForm()

    context={'form':form}
    return render(request, 'social/register.html',context)


            