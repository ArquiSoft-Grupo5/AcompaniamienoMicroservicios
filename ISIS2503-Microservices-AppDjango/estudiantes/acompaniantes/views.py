from .models import Acompaniante
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def AcompanianteList(request):
    queryset = Acompaniante.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def AcompanianteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        acompaniante = Acompaniante()
        acompaniante.name = data_json["name"]
        acompaniante.save()
        return HttpResponse("successfully created acompaniante")