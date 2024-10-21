from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.http.request import HttpRequest

def hello_world(request: HttpRequest):
    return HttpResponse("Hello World")