from django.db import models

from django.utils import timezone
# Create your models here.

class Cyclers(models.Model):
    """ Raspberry pi cycler info
        name: hostname
        url: cycler run address"""
    name =  models.CharField(max_length=7, unique=True)
    url = models.CharField(max_length=30)
    x = models.IntegerField()
    y = models.IntegerField()


class CyclerInput(models.Model):
    """  """
    node = models.ForeignKey(Cyclers, on_delete=models.CASCADE)
    status = models.CharField(max_length=5)
    wafer = models.CharField(max_length=10) # need to change as ForeignKey
    array = models.CharField(max_length=10)
    Tstart = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    Icharge = models.FloatField(default=0.1)         # charge current
    Idischarge = models.FloatField(default=-0.1)        # discharge current
    Vmax = models.FloatField(default=4.2)        # maximum voltage
    Vmin = models.FloatField(default=3.0)        # minimum voltage
    Tstep = models.IntegerField(default=30)     # data acqusition interval
    schedule = models.CharField(max_length=200, default='ocodocodocodo')
