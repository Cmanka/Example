from django.db import connection
from django.shortcuts import render

from labs.forms import Proc1Form
from labs.models import *


def index_view(request):
    return render(request, 'labs/index.html', {'context': 1})


def get_proc1(request):
    if request.method == 'POST':
        hall_name = request.POST.get("hall_name")
        with connection.cursor() as c:
            c.callproc('proc1', [hall_name])
            results = c.fetchall()
        context = {'hall_name': hall_name, 'results': results}
        return render(request, 'labs/proc1dir/result.html', context)
    else:
        query_form = Proc1Form()
        halls = Hall.objects.all()
        query_form.fields['hall_name'].choices = [(name.name, name.name) for name in halls.all()]
        context = {'form': query_form}
        return render(request, 'labs/proc1dir/proc1.html', context)


def get_proc2(request):
    if request.method == 'POST':
        salary = request.POST.get("salary")
        with connection.cursor() as c:
            c.callproc('proc2', [salary])
            results = c.fetchall()
        context = {'salary': salary, 'results': results}
        return render(request, 'labs/proc2dir/result.html', context)
    else:
        return render(request, 'labs/proc2dir/proc2.html')
