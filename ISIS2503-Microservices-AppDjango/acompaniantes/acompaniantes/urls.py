from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^acompaniantes/', views.AcompanianteList, name='acompanianteList'),
    url(r'^acompaniantecreate/$', csrf_exempt(views.AcompanianteCreate), name='acompanianteCreate'),
]