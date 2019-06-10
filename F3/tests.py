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


    def test_boundary_testing(self):
        EE = TransactionalFunction.objects.get(name = "EE")
        
        self.assertEquals(True ,(EE.qt_ALR >= 0 and EE.qt_ALR > -1))
        self.assertEquals(True ,(EE.qt_DER > 0 and EE.qt_DER >= 1))

        CE = TransactionalFunction.objects.get(name = "CE")

        self.assertEquals(True ,(CE.qt_ALR >= 0 and CE.qt_ALR > -1))
        self.assertEquals(True ,(CE.qt_DER > 0 and CE.qt_DER >= 1))

        SE = TransactionalFunction.objects.get(name = "SE")

        self.assertEquals(True ,(SE.qt_ALR >= 0 and SE.qt_ALR > -1))
        self.assertEquals(True ,(SE.qt_DER > 0 and SE.qt_DER >= 1))


    def test_function_points_quantity_false(self):
        obj = TransactionalFunction.objects.get(id=1)
        self.assertNotEqual(obj.function_points, 3)
        obj = TransactionalFunction.objects.get(id=2)
        self.assertNotEqual(obj.function_points, 4)

        obj = TransactionalFunction.objects.create(name = "CE", f_type = 1,
                                             qt_ALR = 14, qt_DER = 5,
                                             function_points = 6,
                                             counter_name = "B",
                                             complexity = "Media")

        self.assertEquals(obj.function_points, 6)

        obj = TransactionalFunction.objects.create(name = "SE", f_type = 1,
                                             qt_ALR = 14, qt_DER = 5,
                                             function_points = 5,
                                             counter_name = "B",
                                             complexity = "Media")

        self.assertEquals(obj.function_points, 5)


