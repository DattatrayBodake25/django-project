from django.contrib import admin
from django.urls import path, include
from items.views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),  # include items app URLs
    path('', api_root),  # root URL returns JSON with all endpoints
]
