from django.shortcuts import render
from Temp.models import Temp
from django.template import RequestContext, loader

# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse

def home(request):
    text = """<h1>Hello World!</h1>
            <p>Whaaaohhhhouuuuu !</p>"""
    return HttpResponse(text)

def testdb(request):
    for item in Temp.objects.all():
        return HttpResponse(item)

def index(request):
    latest_list = Temp.objects.all().order_by('-date')[:5]
    context = {'latest_list': latest_list}
    return render(request, 'Temp/index.html', context)

