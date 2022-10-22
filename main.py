from punto3 import BancoBravos
i = 100
print("**** MENU BANCO****")
print("1: Agregar nuevo cliente")
print("2: Agregar saldo a tu cuenta")
print("3: Quitar saldo a tu cuenta")
print("4: Mostrar saldo de tu cuenta")
print("5: Salir")
while(i != 0):
    i = int(input("Ingrese una opcion del menu: "))
    
    if(i == 1):
        nombre = input("ingresa tu nombre: ")
        apellido = input("ingresa tu apellido: ")
        cedula = input("ingresa tu cedula: ")
        ciudad = input("ingresa tu ciudad: ")
        numeroCuenta = input("ingresa tu numeroCuenta: ")
        saldo = input("ingresa tu saldo: ")
        nuevoUsuario = BancoBravos(nombre,apellido,cedula,ciudad,numeroCuenta,saldo)
    if(i==2):
        saldoAgregar = int(input("Digita el saldo a agregar: "))
        nuevoUsuario.agregarSaldo(saldoAgregar)
    if(i==3):
        saldoQuitar = int(input("Digite el saldo a quitar: "))
        nuevoUsuario.quitarSaldo(saldoQuitar)
    if(i==4):
        nuevoUsuario.mostrarSaldo()
    if(i==5):
        break
    
