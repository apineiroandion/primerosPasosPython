import math
from math import factorial


class Punto:
    """"Clase que representa un punto en el plano"""
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
       return "A coordenada x é: " + str(self.x) + " e a coordenada y é: " + str(self.y)

p1 = Punto(2, 3)
print(p1)

"""No hacen falta metodos de acceso"""
print ("A coordenada x é: ", p1.x)

class Circulo (Punto):
    """Clase que representa un circulo no plano"""
    def __init__(self, radio = 0, x = 0, y = 0):
        super().__init__(x, y)
        self.radio = radio

    def __str__(self):
        return super().__str__() + " e o radio é: " + str(self.radio)

c1 = Circulo(4, 5, 6)
print(c1)

def factorial(n):
    return math.factorial(n)

print(factorial(5))

