"""
URL configuration for demoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect, JsonResponse

# Optional: simple homepage view
def home(request):
    return JsonResponse({
        "message": "Welcome to DemoApp API!",
        "api_root": "/api/"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),  # include our items app
    path('', home),  # root URL returns JSON welcome
    # Alternatively, to redirect root to /api/ instead of JSON:
    # path('', lambda request: HttpResponseRedirect('/api/')),
]
