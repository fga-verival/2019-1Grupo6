from django.db import models
from .constants import *

class TransactionalFunction(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    f_type = models.IntegerField(verbose_name="Functionality type", choices=F_TYPE_CHOICES)
    qt_ALR = models.IntegerField()
    qt_DER = models.IntegerField()
    function_points = models.IntegerField()
    counter_name = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    # TODO: transactional function complexity