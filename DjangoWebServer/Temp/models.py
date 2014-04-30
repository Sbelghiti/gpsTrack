from django.db import models

# Create your models here.
class Temp(models.Model):
    temp = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date")
    
    def __str__(self):
        return "Item({}, {})".format(self.id, self.temp)


