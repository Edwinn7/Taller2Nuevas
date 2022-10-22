ciclistas = []
def recibirDatos ():
    ciclista = {}
    ciclista['nombre'] = input("Nombre: ")
    ciclista['edad'] = input("edad: ")
    ciclista['pais'] = input("pais: ")
    ciclista['equipo'] = input("equipo: ")
    ciclista['tiempo'] = int(input("tiempo: "))
    ciclistas.append(ciclista)

def calcularTiempo ():
    for i in ciclistas:
        tiempomenor = i['tiempo']
        if (tiempomenor > i['tiempo']):
            tiempomenor = i['tiempo']
    print(f"el tiempo menor fue de {tiempomenor}")

print("**** ciclistas****")
print("1: Agregar nuevo ciclista")
print("2: ver mejores tiempos")
print("3: Salir")
i=100
while(i != 0):
    i = int(input("Ingrese una opcion del menu: "))
    if(i==1):
        recibirDatos()
    if(i==2):
        calcularTiempo()
    if(i==3):
        break