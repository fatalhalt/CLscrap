from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import cl


def app(request):
    data, baseurl, keyword = cl.query_craigslist()
    return render(request, 'index.html', {'data': data, 'baseurl': baseurl, 'keyword': keyword})


def page(request):
    return HttpResponse("hello, page!")


def cl_scrap(request):
    if request.method == 'GET':
        arr = cl.query_craigslist()
        ret = {'data': arr, 'items': len(arr)}
        return JsonResponse(ret)