# Pruebas con unittest
import unittest
from complejos import suma_complejos
from complejos import producto_complejos
from complejos import resta_complejos
from complejos import division_complejos
from complejos import modulo_complejos
from complejos import conjugado_complejos
from complejos import cartes_polar
from complejos import polar_cartes
from complejos import fase


# Suma
class TestSumaComplejos(unittest.TestCase):
    def test_suma_positiva(self):
        #(1,2i) + (3,4i) = (4,6i)
        resultado = suma_complejos((1,2),(3,4))
        self.assertEqual(resultado, (4,6))

    def test_suma_negativos(self):
         #(1,-3i) + (2,7) = (3,4)
         resultado = suma_complejos((1, -3),(2, 7))
         self.assertEqual(resultado, (3,4))
    
    def test_suma_ceros(self):
         #(0,0) + (5,8) = (5,8)
         resultado = suma_complejos((0,0),(5,8))
         self.assertEqual(resultado, (5,8))

# Producto
class TestProductoComplejos(unittest.TestCase):
    def test_producto_positivos(self):
        #(1,2i) * (3,4i) = (-5,10i)
        resultado = producto_complejos((1,2),(3,4))
        self.assertEqual(resultado, (-5,10))

    def test_producto_negativos(self):
         #(1,-3i) * (2,-7) = (-19,-13)
         resultado = producto_complejos((1, -3),(2, -7))
         self.assertEqual(resultado, (-19,-13))
    
    def test_producto_ceros(self):
         #(0,0) * (5,-8) = (0,0)
         resultado = producto_complejos((0,0),(5,-8))
         self.assertEqual(resultado, (0,0))

# Resta
class TestRestaComplejos(unittest.TestCase):
    def test_resta_positivos(self):
        #(1,2i) - (3,4i) = (-2,-2i)
        resultado = resta_complejos((1,2),(3,4))
        self.assertEqual(resultado, (-2,-2))

    def test_resta_negativos(self):
         #(1,-3i) - (2,-7) = (-1,4)
         resultado = resta_complejos((1, -3),(2, -7))
         self.assertEqual(resultado, (-1,4))
    
    def test_resta_ceros(self):
         #(0,0) - (5,-8) = (-5,8)
         resultado = resta_complejos((0,0),(5,-8))
         self.assertEqual(resultado, (-5,8))

# División
## Es importante tener en cuenta que para las pruebas de división es necesario contar con todos los decimales.
class TestDivisionComplejos(unittest.TestCase):
    def test_division_positivos(self):
        #(1,2i) / (3,4i) = (0.44,0.08)
        resultado = division_complejos((1,2),(3,4))
        self.assertEqual(resultado, (0.44,0.08))

    def test_division_negativos(self):
         #(1,-3i) / (2,-7) = (0.4339622641509434,0.018867924528301886)
         resultado = division_complejos((1, -3),(2, -7))
         self.assertEqual(resultado, (0.4339622641509434,0.018867924528301886)) 
    
    def test_division_ceros(self):
         #(0,0) / (5,-8) = (0,0)
         resultado = division_complejos((0,0),(5,-8))
         self.assertEqual(resultado, (0,0))

# Módulo
## Es importante tener en cuenta que para las pruebas de división es necesario contar con todos los decimales.
class TestModuloComplejos(unittest.TestCase):
    def test_modulo_positivos(self):
        #(1,2i) = 2.23606797749979
        resultado = modulo_complejos((1,2))
        self.assertEqual(resultado, 2.23606797749979)

    def test_modulo_negativos(self):
         #(-2,-7) = 7.280109889280518
         resultado = modulo_complejos((-2, -7))
         self.assertEqual(resultado, (7.280109889280518)) 
    
    def test_modulo_ceros(self):
         #(0,-8) = 8
         resultado = modulo_complejos((0,-8))
         self.assertEqual(resultado, 8)

# Conjugado
class TestModuloComplejos(unittest.TestCase):
    def test_conjugado_positivos(self):
        #(1,2) = (1,-2)
        resultado = conjugado_complejos((1,2))
        self.assertEqual(resultado, (1,-2))

    def test_conjugado_negativos(self):
         #(-2,-7) = (-2,7)
         resultado = conjugado_complejos((-2, -7))
         self.assertEqual(resultado, (-2,7)) 
    
    def test_conjugado_ceros(self):
         #(0,-8) = (0,8)
         resultado = conjugado_complejos((0,-8))
         self.assertEqual(resultado, (0,8))

# Conversión entre representaciones polar y cartesiano, en los dos sentidos.
## Es importante tener en cuenta que para las pruebas de división es necesario contar con todos los decimales.
class TestCartesPolar(unittest.TestCase):
    def test_cartes_polar_positivos(self):
        #(2,3) = (3.605551275463989, 0.982793723247329)
        resultado = cartes_polar((2,3))
        self.assertEqual(resultado, (3.605551275463989, 0.982793723247329))

    def test_cartes_polar_negativos(self):
         #(-2,-7) = (7.280109889280518,1.2924966677897853)
         resultado = cartes_polar((-2, -7))
         self.assertEqual(resultado, (7.280109889280518,1.2924966677897853)) 
    
    def test_cartes_polar_ceros(self):
         #(-8,0) = (8,0)
         resultado = cartes_polar((-8,0))
         self.assertEqual(resultado, (8,0))

class TestPolarCartes(unittest.TestCase):
    def test_polar_cartes_positivos(self):
        #(3.605551275463989, 0.982793723247329) = (2,3)
        resultado = polar_cartes((3.605551275463989, 0.982793723247329))
        self.assertEqual(resultado, (2,3))

    def test_polar_cartes_negativos(self):
         #(-7.28,-1.29) = (-2.0174399704117394, 6.99487926742021)
         resultado = polar_cartes((-7.28,-1.29))
         self.assertEqual(resultado, (-2.0174399704117394, 6.99487926742021)) 
    
    def test_polar_cartes_ceros(self):
         #(8,0)= (8,0)
         resultado = polar_cartes((8,0))
         self.assertEqual(resultado, (8,0))


# Fase
## Es importante tener en cuenta que para las pruebas de división es necesario contar con todos los decimales.
class TestFaseComplejos(unittest.TestCase):
    def test_fase_positivos(self):
        #(1,2) = 1.1071487177940906
        resultado = fase((1,2))
        self.assertEqual(resultado, 1.1071487177940906)

    def test_fase_negativos(self):
         #(-2,-7) = 1.2924966677897853
         resultado = fase((-2, -7))
         self.assertEqual(resultado, 1.2924966677897853) 
    
    def test_fase_ceros(self):
         #(8,0) = 0
         resultado = fase((8,0))
         self.assertEqual(resultado, 0)
         
if __name__ == "__main__": 
        unittest.main()