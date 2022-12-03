from django.db import models
from account.models import User
from reserve.models import PlayTime
from system.models import System
# Create your models here.

class Payment(models.Model):
    recorder = models.ForeignKey(User,on_delete=models.CASCADE,related_name='records')
    date = models.DateTimeField(auto_now_add=True)
    playtime = models.OneToOneField(PlayTime, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=0)
    system = models.ForeignKey(System, on_delete=models.CASCADE,related_name="records",blank=True, null=True)
