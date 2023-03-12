from django.shortcuts import render
from django.http import HttpResponse

from app.models import Task

# Create your views here.

def index(request): 
    t = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks' : t})