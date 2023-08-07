#Ejercicio 1

"""
from modelo.Vehiculo import Vehiculo

automóvil = Vehiculo(250, 17500)
print("La velocidad máxima del vehículo es:", automóvil.velocidad_maxima,"km/h\nSu kilometraje es de:", automóvil.kilometraje,"km")
"""

#Ejercicio 2-3
"""
from modelo.Punto import Punto

punto_cartesiano = Punto(4,8)
punto_cartesiano.imprimir_coor()

punto_cartesiano.cambiar_coor(0,0)
punto_cartesiano.imprimir_coor()

punto2 = Punto(6,4)
distancia_puntos = punto_cartesiano.distancia(punto2)
print("La distancia entre el punto 1 y punto 2 es:", distancia_puntos," unidades")
"""

#Ejercicio 4
"""
from modelo.Punto import Punto
from modelo.Rectangulo import Rectangulo
punto_inf_izq = Punto(1,0)
punto_sup_der = Punto(5,6)
rectangulo_p = Rectangulo(punto_inf_izq, punto_sup_der)

perimetro = rectangulo_p.perimetro()
area = rectangulo_p.area()
f_cuadrada = rectangulo_p.cuadrado()

print("El perímetro del rectángulo es:", perimetro)
print("El área del rectángulo es:", area)
print("¿Es un cuadrado?", f_cuadrada)
"""

#Ejercicio 5
"""
from modelo.Circulo import Circulo
centro=(4,4)
radio = 4
circulo = Circulo(centro, radio)

print("El área del círculo es de:", circulo.area())
print("El perímetro del círculo es:", circulo.perimetro())

punto_dentro = (1, 1)
print("El punto pertenece al círculo?", circulo.p_pertenece(punto_dentro))
"""

#Ejercicio 6
"""
from modelo.Carta import Carta

carta = Carta(10, Carta.ESPADA)
print("Carta:", carta.valor, carta.pinta)
"""

#Ejercicio 7-11
"""
from modelo.CuentaBancaria import CuentaBancaria
numero_cuenta = "03015205717"
propietario = "Juan Yepes"
balance = 4520000

cuenta = CuentaBancaria(numero_cuenta, propietario, balance)
cuenta.depositar(480000)
cuenta.retirar(1000000)
cuenta.aplicar_cuota_manejo()

cuenta.mostrar_detalles()
"""