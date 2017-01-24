from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

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

def categories_list(request):
    response_data = serializers.serialize('python',Category.objects.all())
    return JsonResponse(response_data, safe=False)

def exercises_list(request):
    response_data = serializers.serialize('python',Exercise.objects.all())
    return JsonResponse(response_data, safe=False)


