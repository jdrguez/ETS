import pytest

from formas import Triangulo, Cuadrado, Coche

def test_area_triangulo():
    triangulo = Triangulo(12, 19)   
    assert triangulo.area() == 228

def test_area_cuadrado():
    cuadrado = Cuadrado(10, 10)
    assert cuadrado.area_cuadrado() == 100

def test_mult_cilindradra():
    coche = Coche('Toyota', 100)
    assert coche.mult_cilindrada(10) == 1000