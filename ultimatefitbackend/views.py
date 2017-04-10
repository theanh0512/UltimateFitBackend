# Create your views here.
import datetime
import json
import math

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
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


def categories_list(request):
    response_data = serializers.serialize('python', Category.objects.all())
    return JsonResponse(response_data, safe=False)


def exercises_list(request, page):
    page = int(page)
    numObject = Exercise.objects.count()
    numPage = math.ceil(numObject / 10)

    exercise_list = Exercise.objects.all()
    paginator = Paginator(exercise_list, 10)  # Show 10 exercises per page

    # page = request.GET.get('page')
    try:
        exercises = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exercises = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exercises = paginator.page(paginator.num_pages)

    data = {'array': [o.dump() for o in exercises], 'page': paginator.num_pages}
    json_result = json.dumps(data)

    return HttpResponse(json_result)


def exercises_list_with_date(request, page, date):
    page = int(page)
    date = float(date)
    modified_date_time = datetime.datetime.fromtimestamp(date / 1000)
    today = datetime.date.today() + datetime.timedelta(days=1)
    exercise_list = Exercise.objects.filter(modified_datetime__range=[modified_date_time, today])
    paginator = Paginator(exercise_list, 10)  # Show 10 exercises per page

    # page = request.GET.get('page')
    try:
        exercises = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        exercises = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        exercises = paginator.page(paginator.num_pages)

    data = {'array': [o.dump() for o in exercises], 'page': paginator.num_pages}
    json_result = json.dumps(data)

    return HttpResponse(json_result)
