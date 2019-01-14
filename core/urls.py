from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


app_name ="core"

urlpatterns = [
        url(r'^$', views.homepage),
        url(r'^szerviz/', views.szerviz, name='szerviz'),
        url(r'^markak/', views.brands, name='markak'),

]
