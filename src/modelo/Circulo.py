import math
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2
    
    def perimetro(self):
        return 2*math.pi * self.radio
    
    def p_pertenece(self, punto):
        distancia_cp = math.sqrt((punto[0]-self.centro[0])**2 + (punto[1]-self.centro[1])**2)
        return distancia_cp <= self.radio
    