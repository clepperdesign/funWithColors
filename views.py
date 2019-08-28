from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello world </h1>")
def detail(request, colorname):
    #return HttpResponse("You're looking at color %s." % colorname)
    return HttpResponse('<body bgcolor=%s>' % colorname)