from .models import Cita
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_acompaniante(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    acompaniantes = r.json()
    for acompaniante in acompaniantes:
        if data["acompaniante"] == acompaniante["id"]:
            return True
    return False

def CitaList(request):
    queryset = Cita.objects.all()
    context = list(queryset.values('id', 'acompaniante', 'value', 'unit', 'place', 'dateTime'))
    return JsonResponse(context, safe=False)

def CitaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_acompaniante(data_json) == True:
            cita = Cita()
            cita.acompaniante = data_json['acompaniante']
            cita.value = data_json['value']
            cita.unit = data_json['unit']
            cita.place = data_json['place']
            cita.save()
            return HttpResponse("successfully created cita")
        else:
            return HttpResponse("unsuccessfully created cita. Acompaniante does not exist")