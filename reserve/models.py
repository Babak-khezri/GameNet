from django.db import models
from system.models import System

# Create your models here.

class PlayTime(models.Model):
    system = models.ForeignKey(System,on_delete=models.CASCADE,related_name='play_times',null=True,verbose_name='سیستم')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=False ,null=True, blank=True)



