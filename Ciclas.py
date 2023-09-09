import os

usuarios = {}

prestamos = []

os.system('cls' if os.name == 'nt' else 'clear')

def registrar_usuario():

    numero_cedula = input("Ingrese el número de la cedula: ")
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios[numero_cedula] = {'nombre': nombre, 'contrasena': input("Ingrese la contraseña del usuario: ")}
    print("______________________________________________________________")
    print(f"\nUsuario registrado: {nombre} (Cedula: {numero_cedula}).")

def tomar_bicicleta(numero_cedula):

    origen = input("Ingrese el origen del viaje: ")
    destino = input("Ingrese el destino del viaje: ")
    prestamos.append({
        'usuario': usuarios[numero_cedula]['nombre'],
        'origen': origen,
        'destino': destino
    })
    print(f"{usuarios[numero_cedula]['nombre']}: ha cogido una cicla de {origen} -> {destino}")

def consultar_listado_usuarios():

    print("____________________________________________________")
    print("Listado de Usuarios:")

    for numero_cedula, datos in usuarios.items():
        print(f"Cedula: {numero_cedula} , Nombre: {datos['nombre']}")

def consultar_listado_prestamos():

    print("____________________________________________________")
    print("Listado de Préstamos:")

    for prestamo in prestamos:
        print(f"\nUsuario: {prestamo['usuario']} | Origen: {prestamo['origen']} -> Destino: {prestamo['destino']}")

while True:

    print("____________________________________________________")
    print("\n    Sistema Prestamos de ciclas de la Ciudad")
    print("\n1. Registrar Usuario")
    print("2. Tomar Bicicleta")
    print("3. Consultar Listado de Usuarios")
    print("4. Consultar Listado de Préstamos")
    print("5. Salir")
    print("_____________________________________________________")
    opcion = input("Seleccione una opción: ")

    os.system('cls' if os.name == 'nt' else 'clear')
    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        numero_cedula = input("Ingrese el número de la cedula: ")
        if numero_cedula in usuarios:
            tomar_bicicleta(numero_cedula)
        else:
            print("_________________________________________________________")
            print("Usuario no registrado. Por favor, regístrese primero.")

    elif opcion == '3':
        consultar_listado_usuarios()
    elif opcion == '4':
        consultar_listado_prestamos()
    elif opcion == '5':

        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción no invalida. Por favor, seleccione una opción válida.")
