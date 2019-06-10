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

    def getFunctionPoints(self):
        if (self.f_type == 0):
            if (self.qt_ALR <= 1):
                if (self.qt_DER <= 15):
                    self.complexity = "Baixa"
                else:
                    self.complexity = "Media"
            elif (self.qt_ALR == 2):
                if (self.qt_DER >= 1 and self.qt_DER <= 4):
                    self.complexity = "Baixa"
                elif (self.qt_DER >= 5 and self.qt_DER <= 15):
                    self.complexity = "Media"
                elif (self.qt_DER > 15):
                    self.complexity = "Alta"
            else:
                if (self.qt_DER < 5): 
                    self.complexity = "Media"
                else:
                    self.complexity = "Alta"
            pf_dict = {'Baixa': 3, 'Media': 4, 'Alta': 6 }

            self.function_points = pf_dict[self.complexity]

        if (self.f_type == 1):
            if (self.qt_ALR <= 1):
                if (self.qt_DER <= 15):
                    self.complexity = "Baixa"
                else:
                    self.complexity = "Media"
            elif (self.qt_ALR == 2 and self.qt_ALR == 3):
                if (self.qt_DER >= 1 and self.qt_DER <= 4):
                    self.complexity = "Baixa"
                elif (self.qt_DER >= 5 and self.qt_DER <= 19):
                    self.complexity = "Media"
                elif (self.qt_DER > 20):
                    self.complexity = "Alta"
            else:
                if (self.qt_DER < 5): 
                    self.complexity = "Media"
                else:
                    self.complexity = "Alta"

            pf_dict = {'Baixa': 3, 'Media': 4, 'Alta': 6 }

            self.function_points = pf_dict[self.complexity]

        if (self.f_type == 2):
            if (self.qt_ALR <= 1):
                if (self.qt_DER <= 20):
                    self.complexity = "Baixa"
                else:
                    self.omplexity = "Media"
            elif (self.qt_ALR == 2 and self.qt_ALR == 3):
                if (self.qt_DER >= 1 and self.qt_DER <= 5):
                    self.complexity = "Baixa"
                elif (self.qt_DER >= 6 and self.qt_DER <= 19):
                    self.complexity = "Media"
                elif (qt_DER > 20):
                    self.complexity = "Alta"
            else:
                if (self.qt_DER < 6): 
                    self.complexity = "Media"
                else:
                    self.complexity = "Alta"

            pf_dict = {'Baixa': 4, 'Media': 5, 'Alta': 7 }

            self.function_points = pf_dict[self.complexity]