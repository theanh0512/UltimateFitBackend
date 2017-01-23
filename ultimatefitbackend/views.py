from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def exercise(request, id):
    template = loader.get_template('exercise.html')
    context = {
        'exercise': Exercise.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))
