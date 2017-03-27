from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import cl


def app(request):
    return HttpResponse("hello, app!")


def page(request):
    return HttpResponse("hello, page!")


def cl_scrap(request):
    if request.method == 'GET':
        arr = cl.query_craigslist()
        ret = {'data': arr, 'items': len(arr)}
        return JsonResponse(ret)