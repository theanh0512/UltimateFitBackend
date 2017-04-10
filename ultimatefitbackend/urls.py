"""ultimatefit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'exercise/(?P<id>[0-9]+)$', views.exercise, name='exercise'),
    url(r'categories-list$', views.categories_list, name='categories_list'),
    url(r'exercises-list/(?P<page>[0-9]+)$', views.exercises_list, name='exercises_list'),
    url(r'exercises-list/(?P<date>[0-9]+)/(?P<page>[0-9]+)$', views.exercises_list_with_date,
        name='exercises_list_with_date'),
]
