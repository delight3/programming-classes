from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Students


# Create your views here.
def greeting(request):
    return HttpResponse('good day class')


def index(request):
    user = Students.objects.all().values()
    template = loader.get_template("index.html")

    context = {
        'user': user,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    user = Students.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'user': user
    }
    
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())
