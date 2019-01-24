from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'^szerviz/',include('core.urls')),
    url(r'^kapcsolat/',include('core.urls')),
    url(r'^mitsubishi/',include('core.urls')),
]
