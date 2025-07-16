
inventario = {}

def ingreso_productos():
    print("\n---Ingreso de productos---")
    s = False
    while s == False:
        try:
            cantidad = int(input("Cuantos productos desea ingresar: "))
            if cantidad > 0:
                s = True
            else:
                print("La cantidad debe de ser mayor a 0")
        except ValueError:
            print("Ingrese un numero valido")
    for i in range(cantidad):
        s = False
        while s == False:
            try:
                codigo = int(input(f"Ingrese el codigo del producto {i+1}: "))
                if codigo not in inventario:
                    s = True
                else:
                    print("El codigo es invalido porque ya esta registrado en otro producto")
            except ValueError:
                print("El codigo debe de ser un numero valido")
        nombre = input(f"Ingrese el nombre del producto {i+1}: ")
        s = False
        while s == False:
            categoria = input(f"Ingrese la categoria del producto (Hombre, Mujer, Niño) {i+1}: ").lower()
            if categoria in ["hombre", "mujer", "niño"]:
                s = True
            else:
                print("Categoria invalida")
        s = False
        while s == False:
            talla = input(f"Ingrese la talla del producto, (S, M, L, XL) {i+1}: ").upper()
            if talla in ["S", "M", "L", "XL"]:
                s = True
            else:
                print("Talla invalida")
        s = False
        while s == False:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio > 0:
                    s = True
                else:
                    print("El precio del producto debe de ser mayor a 0...")
            except ValueError:
                print("Ingrese un numero valido para el precio")

        s = False
        while s == False:
            try:
                stock = int(input(f"Ingrese el stock del producto {i+1} en tienda: "))
                if stock >= 0:
                    s = True
                else:
                    print("El stock no puede ser un numero negativo")
            except ValueError:
                print("Ingrese un numero valio para el stock")

        inventario[codigo] = {
            "Nombre": nombre,
            "Categoria": categoria,
            "Talla": talla,
            "Precio": precio,
            "Stock": stock
        }
        print("Se ha registrado el producto")

def buscar_productos():
    print("---Buscar productos---")
    buscar = int(input("Ingrese el codigo del producto que desea buscar: "))
    if buscar in inventario:
        print(f"Nombre: {inventario[buscar] ['Nombre']},  Categoria: {inventario[buscar] ['Categoria']}, Talla: {inventario[buscar] ['Talla']}, Precio: {inventario[buscar] ['Precio']}, Stock; {inventario[buscar] ['Stock']}")
    else:
        print("El producto que ingreso no existe")

def categorias():
    stock_hombres = 0
    stock_mujeres = 0
    stock_ninos = 0

    for i in inventario.values():
        categoria = i["Categoria"].lower()
        if categoria == "hombre":
            stock_hombres += i["Stock"]
        elif categoria == "mujer":
            stock_mujeres += i["Stock"]
        elif categoria == "niño":
            stock_ninos += i["Stock"]

    print("---Stock por categoria---")
    print(f"Hombre: {stock_hombres} unidades")
    print(f"Mujer: {stock_mujeres} unidades")
    print(f"Niño: {stock_ninos} unidades")

def valor_total_inventario():
    suma = 0
    for i in inventario.values():
        suma += i["Precio"] * i["Stock"]
    print(f"El valor total del inventario es de: Q{suma}")

def lista_completa_productos():
    if len(inventario) > 0:
        print("---Inventario---")
        for codigo, datos in inventario.items():
            print(f"Codigo: {codigo}")
            print(f"  Nombre: {datos['Nombre']}")
            print(f"  Categoria: {datos['Categoria']}")
            print(f"  Talla: {datos['Talla']}")
            print(f"  Precio: Q{datos['Precio']}")
            print(f"  Stock: {datos['Stock']} unidades")
            print("-------------------------------")

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
            ingreso_productos()
        case 2:
            buscar_productos()
        case 3:
            categorias()
        case 4:
            valor_total_inventario()
        case 5:
            lista_completa_productos()
        case 6:
            print("Gracias por usar el sistema...")
            a = True
        case _:
            print("Opcion invalida")