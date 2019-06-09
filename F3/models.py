from django.db import models
from .constants import *

class TransactionalFunction(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=200,blank=False)
    f_type = models.IntegerField(verbose_name="Tipo de funcionalidade", choices=F_TYPE_CHOICES,blank=False,default=0)
    qt_ALR = models.IntegerField(verbose_name="Quantidade de ALR", blank=False)
    qt_DER = models.IntegerField(verbose_name="Quantidade de DER", blank=False)
    function_points = models.IntegerField(verbose_name="Pontos de Função")
    counter_name = models.CharField(verbose_name="Nome do contador", max_length=200)
    date = models.DateField(auto_now=True)
    complexity = models.CharField(verbose_name="Complexidade", max_length=50, choices=COMPLEXITY_CHOICES)

    def __str__(self):
        return self.name