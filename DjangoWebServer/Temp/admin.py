from django.contrib import admin

# Register your models here.

#To access to Temp data base on navigator
from Temp.models import Temp
admin.site.register(Temp)