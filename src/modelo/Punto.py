import math
class Punto:
    def __init__(self, eje_x, eje_y):
        self.x = eje_x
        self.y = eje_y

    def imprimir_coor(self):
        print("Las coordenadas del punto son:\n", self.x, ",", self.y)
    
    def cambiar_coor(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def distancia(self, punto2):
        calculo = math.sqrt((punto2.x-self.x)**2+(punto2.y-self.y)**2)
        return calculo