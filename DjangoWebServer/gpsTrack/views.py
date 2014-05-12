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
        print ("this is a post method")
        qdict = QueryDict(request.body)
        print (qdict)
        lat = qdict.get('slot_latitude')
        print lat
        lon = qdict.get('slot_longitude')
        coord = lat+','+lon
        print coord
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
    
def getGPSmapLine(request):
        #new google.maps.LatLng(58.983991,5.734863);
        #coord = gps.objects.last()
        #context = {'latest_coord' : coord}
        latest_list = gps.objects.all().order_by('-date')
        coord_list = ""
        i=0
        for element in latest_list:
            var = 'new google.maps.LatLng(%s,%s)' % (element.latitude,element.longitude)
            if i == 0 : 
                coord_list += var
            elif i > 0 :
                coord_list += ","+var
            i = i+1
            #coord_list.append(var)
            #coord_list +=var+","
        #coord_list += "]"
        print (coord_list)
        
        print (latest_list)
        print (list)
            
        context = {'latest_list' : latest_list,'coord_list' : coord_list}
        return render(request,'gpsTrack/googlemapLine2.html',context)
        #return render(request,'gpsTrack/test.html',context)
        
        
        
    
    