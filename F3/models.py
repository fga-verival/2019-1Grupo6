from django.db import models
from .constants import *

class TransactionalFunction(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200,blank=False)
    f_type = models.IntegerField(verbose_name="Functionality type", choices=F_TYPE_CHOICES,blank=False)
    qt_ALR = models.IntegerField(blank=False)
    qt_DER = models.IntegerField(blank=False)
    function_points = models.IntegerField()
    counter_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    complexity = models.CharField(max_length=50, choices=COMPLEXITY_CHOICES)

    def __str__(self):
        return self.name