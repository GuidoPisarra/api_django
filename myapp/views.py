from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello world")


def hello2(request):
    return HttpResponse("<h1>Hello world</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")
