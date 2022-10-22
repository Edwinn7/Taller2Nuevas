class BancoBravos:
    def __init__(self,nombre,apellido,cedula,ciudad,numeroCuenta,saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.ciudad = ciudad
        self.numeroCuenta = numeroCuenta
        self.saldo = int(saldo)
    def agregarSaldo(self,saldoAgregar):
        self.saldo += saldoAgregar
    def quitarSaldo(self,saldoQuitar):
        self.saldo = self.saldo-saldoQuitar
    def mostrarSaldo(self):
        print(f'El saldo actual de {self.nombre} es de {self.saldo}')