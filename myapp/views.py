from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def app(request):
    return HttpResponse("hello, app!")


def page(request):
    return HttpResponse("hello, page!")