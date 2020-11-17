from django.urls import path

from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('proc/1', get_proc1, name='proc1'),
    path('proc/2', get_proc2, name='proc2'),
]
