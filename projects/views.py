from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Projects

def index(request):
    myprojects = Projects.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'myprojects': myprojects,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('create_project.html')
    return HttpResponse(template.render({}, request))

def add(request):
    x = request.POST['name']
    y = request.POST['start_date']
    z = request.POST['end_date']
    project = Projects(name=x, start_date=y, end_date=z)
    project.save()
    return HttpResponseRedirect(reverse('index'))