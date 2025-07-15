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