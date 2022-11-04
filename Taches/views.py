from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from Taches.models import Task

# Create your views here.


def home(request):
    """ la vue qui permet de recupérer tous les objets dans la bd et l'affiche de la template"""
    tasks = Task.objects.all()
    return render(request, 'list.html', locals())


def task_listing(request):
    objets = Task.objects.all().order_by("-due_date")
    
    return render(request, "list2.html", {"taches":objets})
    
