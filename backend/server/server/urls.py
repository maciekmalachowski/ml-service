# backend/server/server/urls.py file
from django.urls import re_path, include
from django.contrib import admin
from django.urls import path

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns