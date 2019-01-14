from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'cars'

urlpatterns = [
        url(r'^$', views.car_list, name="list"),
        url(r'^(?P<slug>[\w-]+)/$',views.car_detail, name="detail"),
]
#name capturing group for urls
#Freihof1478963Humu7894I3gnHX0UYP
#\w any kind of character letterbnubers
#- hyphen included
#+ any length
#slug is can be everythong like abs or seggs
