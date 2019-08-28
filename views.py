from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Color
# Create your views here.
#def index(request):
    #return HttpResponse("<h1>Hello world </h1>")
def detail(request, colorname):
    return HttpResponse('<body bgcolor=%s>' % colorname)
def index(request):
    colorslist =  Color.objects.all()
    template = loader.get_template('colortime/index.html')
    context = {
        'colorslist': colorslist,
    }
    return HttpResponse(template.render(context, request))

