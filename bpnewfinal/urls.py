from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'^szerviz/',include('core.urls')),
    url(r'^markak/',include('core.urls')),
    url(r'^kapcsolat/',include('core.urls')),


]
