from django import views
from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("this is totototo ")

