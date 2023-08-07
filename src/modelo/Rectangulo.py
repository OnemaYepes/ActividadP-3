import math

class Rectangulo:
    def __init__(self, punto_inf_izq, punto_sup_der):
        self.punto_inf_izq = punto_inf_izq
        self.punto_sup_der = punto_sup_der

    def longitud_lados(self):
        base = abs(self.punto_sup_der.x - self.punto_inf_izq.x)
        altura = abs(self.punto_sup_der.y - self.punto_inf_izq.y)
        return base, altura
    
    def perimetro(self):
        base, altura = self.longitud_lados()
        return 2*(base+altura)
    
    def area(self):
        base, altura = self.longitud_lados()
        return base*altura
    
    def cuadrado(self):
        base, altura = self.longitud_lados()
        return base == altura