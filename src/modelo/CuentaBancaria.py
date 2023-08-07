class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        self.movimientos = []
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            self.movimientos.append(f"Depósito de ${cantidad}")
            return True
        else: 
            return False
        
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.balance:
            self.balance -= cantidad
            self.movimientos.append(f"Retiro de ${cantidad}")
            return True
        else:
            return False
        
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        self.movimientos.append(f"Cuota de manejo de ${cuota}")
        return cuota
    
    def mostrar_detalles(self):
        print("-----------Detalles de la cuenta-----------")
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)
        print("Movimientos:")
        for x in self.movimientos:
            print(x)
