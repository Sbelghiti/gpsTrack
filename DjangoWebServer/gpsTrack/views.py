from django.shortcuts import render

# Create your views here.
from gpsTrack.models import gps
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict

# Create your views here.
#-*- coding: utf-8 -*-
from django.http import HttpResponse

@csrf_exempt
def post(request):
    if request.method == 'POST':
        qdict = QueryDict(request.body)
        lat = qdict.get('slot_latitude')
        lon = qdict.get('slot_longitude')
        coord = lat+','+lon
        new_coord = gps(latitude=lat,longitude=lon)
        new_coord.save()
        return HttpResponse(coord)
    elif request.method == "GET":
        print("this is a get method")
        return HttpResponse('This is a GET method')
    
def getGPSCoord(request):
        coord = gps.objects.last()
        context = {'latest_coord' : coord}
        return render(request,'gpsTrack/googlemap.html',context)