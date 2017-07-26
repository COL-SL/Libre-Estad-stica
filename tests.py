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


    def tearDown(self):
        del self.pyapp



if __name__ == '__main__':
    main()