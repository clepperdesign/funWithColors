from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Color, ColorForm

def detail(request, colorname):
    bodybg = colorname
    colorslist =  Color.objects.all()
    context = {
        'bodybg' : bodybg,
        'colorslist' : colorslist,
    }
    template = loader.get_template('colortime/detail.html')
    return HttpResponse(template.render(context, request))
    #return HttpResponse('<body bgcolor=%s>' % colorname)
def index(request):
    colorslist =  Color.objects.all()
    template = loader.get_template('colortime/index.html')
    context = {
        'colorslist': colorslist,
    }
    return HttpResponse(template.render(context, request))