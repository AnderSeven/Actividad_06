inventario = {}

def ingreso_productos():
    print("\n---Ingreso de productos---")
    cantidad = int(input("Cuantos productos desea ingresar: "))
    if cantidad > 0:
        for i in range(cantidad):
            codigo = int(input(f"Ingrese el codigo del producto {i+1}: "))
            nombre = input(f"Ingrese el nombre del producto {i}: ")
            categoria = input(f"Ingrese la categoria del producto (Hombre, Mujer, Niño) {i}: ")


opciones = 0
a = False
while a == False:
    print("---Menu---")
    print("1. Ingrese productos")
    print("2. Buscar productos")
    print("3. Categorias")
    print("4. Valor total del inventario Q")
    print("5. Lista completa de productos")
    print("6. Salir")
    opciones = int(input("Elija una opcion: "))
    match opciones:
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            print("Gracias por usar el sistema...")
            a = True
        case _:
            print("Opcion invalida")