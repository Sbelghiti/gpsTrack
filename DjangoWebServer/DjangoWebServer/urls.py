from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWebServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', 'Temp.views.home'),
    url(r'^testdb/$', 'Temp.views.testdb'),
    url(r'^admin/', include(admin.site.urls)),      #to access to database on navigator
    url(r'^index/' , 'Temp.views.index'),
    url(r'^postgps*' , 'gpsTrack.views.post'),
    url(r'^map/', 'gpsTrack.views.getGPSCoord')
)
