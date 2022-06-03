from .models import Financiero
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_estudiante(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    estudiantes = r.json()
    for estudiante in estudiantes:
        if data["estudiante"] == estudiante["id"]:
            return True
    return False

def FinancieroList(request):
    queryset = Financiero.objects.all()
    context = list(queryset.values('id', 'estudiante', 'value', 'unit', 'place', 'dateTime'))
    return JsonResponse(context, safe=False)

def FinancieroCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_estudiante(data_json) == True:
            financiero = Financiero()
            financiero.estudiante = data_json['estudiante']
            financiero.value = data_json['value']
            financiero.unit = data_json['unit']
            financiero.place = data_json['place']
            financiero.save()
            return HttpResponse("successfully created financiero")
        else:
            return HttpResponse("unsuccessfully created financiero. Estudiante does not exist")