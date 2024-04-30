import pytest 
from calculadora import sum_number, sub_number, mul_number, div_number

def test_sum_number():
    assert sum_number(2, 2) == 4



def test_mul_number():
    assert mul_number(2, 1) == 2

def test_div_number():
    assert div_number(3,1) == 3.0


def test_sub_number():
    assert sub_number(3, 2) == 1