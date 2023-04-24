import requests
import json
from django.shortcuts import redirect, render
from .models import *
from .forms import UserREgisterForm
from django.contrib import messages


def inicio(request):
    #return render(request, 'social/feed.html', {'nombre':nombre})
    private_key = "ae44c373a40cae4d4393c7eb5af469e3324f0c82"
    public_key = "620661ca732f53b2798f48cfef87e595"
    hashed = "2a47b76bda75a7fcf941a067b556ea90"
    laurl = "https://gateway.marvel.com:443/v1/public/characters?ts=1&apikey=620661ca732f53b2798f48cfef87e595&hash=2a47b76bda75a7fcf941a067b556ea90"
    lista = []
    response = requests.get(laurl)
    if response.status_code==200:
        response_json = json.loads(response.text)
        for i in response_json["data"]["results"]:
            idcomic = i["id"]
            nombre = i["name"]
            imagen = i["thumbnail"]["path"]
            extension = i["thumbnail"]["extension"]
            dic = {"nombre":nombre,"imagen":imagen,"extension":extension,"id":idcomic}
            lista.append(dic)

    return render(request, 'social/feed.html' , {'comics_marvel':lista})

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


            