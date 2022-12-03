from django.db import models

# Create your models here.


class System(models.Model):
    is_busy = models.BooleanField(default=False)
    name = models.CharField(max_length=100,unique=True)
    ram = models.IntegerField()
    graphic = models.IntegerField()
    cost_per_hour = models.DecimalField(max_digits=10,decimal_places=0)

    def __str__(self):
        return self.name
    
    