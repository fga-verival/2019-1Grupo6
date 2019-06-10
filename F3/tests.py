from django.test import TestCase
from .models import TransactionalFunction
# Create your tests here.


class TransactionalFunctionTestCase(TestCase):

    def setUp(self):
        TransactionalFunction.objects.create(name = "EE", f_type = 0,
                                             qt_ALR = 2, qt_DER = 4,
                                             function_points = 1,
                                             counter_name = "A",
                                             complexity = "Baixa")
        TransactionalFunction.objects.create(name = "CE", f_type = 1,
                                             qt_ALR = 2, qt_DER = 5,
                                             function_points = 1,
                                             counter_name = "B",
                                             complexity = "Media")
        TransactionalFunction.objects.create(name = "SE", f_type = 2,
                                             qt_ALR = 4, qt_DER = 6,
                                            function_points = 1,
                                             counter_name = "C",
                                             complexity = "Alta")

    def test_is_funcionalComplexity_EE(self):
        EE = TransactionalFunction.objects.get(name = "EE")
        self.assertEquals(0, EE.f_type)

    def test_is_funcionalComplexity_CE(self):
        CE = TransactionalFunction.objects.get(name = "CE")
        self.assertEquals(1, CE.f_type)

    def test_is_funcionalComplexity_SE(self):
        SE = TransactionalFunction.objects.get(name = "SE")
        self.assertEquals(2, SE.f_type)

    def test_is_right_complexity(self):
        EE = TransactionalFunction.objects.get(name = "EE")
        CE = TransactionalFunction.objects.get(name = "CE")
        SE = TransactionalFunction.objects.get(name = "SE")

        ee_complexity = EE.complexity
        ce_complexity = CE.complexity
        se_complexity = SE.complexity

        EE.getFunctionPoints()
        CE.getFunctionPoints()
        SE.getFunctionPoints()

        self.assertEquals(ee_complexity, EE.complexity)
        self.assertEquals(ce_complexity, CE.complexity)
        self.assertEquals(se_complexity, SE.complexity)



