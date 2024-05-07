class Triangulo:
    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height

class Cuadrado:
    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def area_cuadrado(self):
        return self.base * self.height

class Coche:
    def __init__(self, marca: str, cilindrada: int):
        self.marca = marca
        self.cilindrada = cilindrada
    
    def mult_cilindrada(self, num: int):
        return self.cilindrada * num