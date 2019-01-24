from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views



urlpatterns = [
        url(r'^$', views.homepage),
        url(r'^szerviz/', views.szerviz, name='szerviz'),
        url(r'^kapcsolat/', views.kapcsolat, name='kapcsolat'),
        url(r'^mitsubishi/', views.mitsu, name='mitsubishi'),



]
