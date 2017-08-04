from unittest import TestCase, main
from gui import PyApp


class PyAppTest(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        self.pyapp = PyApp()

    def test_calcular_rango(self):
        valor_maxino = 10
        valor_minimo = 5
        self.assertEqual(self.pyapp.calcular_rango(valor_maxino, valor_minimo), 5)

        valor_maxino = 100
        self.assertEqual(self.pyapp.calcular_rango(valor_maxino, valor_minimo), 95)
        self.assertNotEqual(self.pyapp.calcular_rango(valor_maxino, valor_minimo), 900)


    def test_calcular_mediana(self):
        array = [9, 3, 15, 11]
        self.assertEqual(self.pyapp.calcular_mediana(array), 10)
        self.assertNotEqual(self.pyapp.calcular_mediana(array), 9)

        array = [5, 3, 2, 2, 5, 5, 6, 9, 8]
        self.assertEqual(self.pyapp.calcular_mediana(array), 5)
        self.assertNotEqual(self.pyapp.calcular_mediana(array), 9)

        array = [5, 3, 6, 5, 4, 5, 2, 8, 6, 5, 4, 8, 3, 4, 5, 4, 8, 2, 5, 4]
        self.assertEqual(self.pyapp.calcular_mediana(array), 5)
        self.assertNotEqual(self.pyapp.calcular_mediana(array), 9)


    def test_calcular_varianza(self):
        array = [2, 3, 6, 8, 11]
        self.assertEqual(self.pyapp.calcular_varianza(array), 10.8)
        self.assertNotEqual(self.pyapp.calcular_varianza(array), 9)

        array = [12, 6, 7, 3, 15, 10, 18, 5]
        self.assertEqual(self.pyapp.calcular_varianza(array), 23.75)
        self.assertNotEqual(self.pyapp.calcular_varianza(array), 9)

        array = [9, 3, 8, 8, 9, 8, 9, 18]
        self.assertEqual(self.pyapp.calcular_varianza(array), 15)
        self.assertNotEqual(self.pyapp.calcular_varianza(array), 9)


    def test_desviacion_tipica(self):
        array = [9, 3, 8, 8, 9, 8, 9, 18]
        self.assertEqual(self.pyapp.calcular_desviacion_tipica(array), 3.872983346207417)
        self.assertNotEqual(self.pyapp.calcular_desviacion_tipica(array), 9)

        array = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012,
                 2013, 2014, 2015, 2016, 2017]
        self.assertEqual(self.pyapp.calcular_desviacion_tipica(array), 6.3442887702247601)
        self.assertNotEqual(self.pyapp.calcular_desviacion_tipica(array), 9)

        array = [2, 3, 6, 8, 11]
        self.assertEqual(self.pyapp.calcular_desviacion_tipica(array), 3.2863353450309969)
        self.assertNotEqual(self.pyapp.calcular_desviacion_tipica(array), 9)

    def test_calulcar_suma(self):
        array = [40, 5, 80, 3]
        self.assertEqual(self.pyapp.calcular_suma(array), 128)
        self.assertNotEqual(self.pyapp.calcular_suma(array), 9)

        array = [9, -8, 9, -8]
        self.assertEqual(self.pyapp.calcular_suma(array), 2)
        self.assertNotEqual(self.pyapp.calcular_suma(array), 9)

        array = [2, 3, 6, 8, 11]
        self.assertEqual(self.pyapp.calcular_suma(array), 30)
        self.assertNotEqual(self.pyapp.calcular_suma(array), 9)


    def tearDown(self):
        del self.pyapp


if __name__ == '__main__':
    main()
