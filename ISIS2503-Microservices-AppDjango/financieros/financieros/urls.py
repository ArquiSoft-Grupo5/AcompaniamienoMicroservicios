from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^financieros/', views.FinancieroList),
    url(r'^financierocreate/$', csrf_exempt(views.FinancieroCreate), name='financieroCreate'),
]