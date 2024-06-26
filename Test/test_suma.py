import pytest 
from sumar import sum_number, is_greater_than, max_value, sub_number, Empleado, mul_number, div_number

def test_sum_number():
    assert sum_number(2, 2) == 4

def test_max_value():
    assert max_value([4,5,6,7,8,9]) == 9
#def test_greater_than():
#   assert is_greater_than(3, 2)

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5,1,6),
          (6, sum_number(4,2), 12),
          (sum_number(19,1),15,35),
          (-7,10, sum_number(-7,10)),
    ]
)

def test_sum_number_params(input_x, input_y, expected):
    assert sum_number(input_x, input_y) == expected

@pytest.mark.parametrize(
    "input_x, expected",
    [
        ([4, 10, 89, 7, 103], 103),
          ([988, 56, 1003, 3210321, 00], 3210321),
    ]
)

def test_max_params(input_x, expected):
    assert max_value(input_x) == expected

def test_sub_number():
    assert sub_number(3, 2) == 1


def test_aumentar_salario():
    empleado = Empleado('Carlos', 'Perez', 3000)
    empleado.aumentar_salario()

    assert empleado.salario == 4000


def test_mul_number():
    assert mul_number(2, 1) == 2

def test_div_number():
    assert div_number(3,1) == 3.0

