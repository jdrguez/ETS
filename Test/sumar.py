def sum_number(num1: int, num2: int) -> int:
    return num1 + num2 


def is_greater_than(num1:int, num2:int) -> bool:
    return num1 > num2


def max_value(values: list) -> int:
    return max(values)

def sub_number(n1: int, n2: int) -> int:
    return n1 - n2

def mul_number(n1:int, n2: int) -> int:
    return n1 * n2

def div_number(n1: int, n2: int) -> float:
    return n1 / n2

class Empleado:
    def __init__(self, nombre:str, apellidos: str, salario: int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.salario = salario
    
    def aumentar_salario(self):
        self.salario += 1000