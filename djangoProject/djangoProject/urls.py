from django.contrib import admin
from django.urls import path, include

from labs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('labs.urls')),
]
