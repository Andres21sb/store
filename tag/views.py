from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_tag(request):
    return HttpResponse('Inside Tag')