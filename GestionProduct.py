productos = []  

def anadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un valor numérico para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce un número entero para la cantidad.")
    
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.\n")

def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("\nNo hay productos en el inventario.\n")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']}")

            nuevo_nombre = input("Introduce el nuevo nombre (o deja en blanco para no cambiar): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre

            while True:
                nuevo_precio = input("Introduce el nuevo precio (o deja en blanco para no cambiar): ")
                if nuevo_precio:
                    try:
                        producto['precio'] = float(nuevo_precio)
                        break
                    except ValueError:
                        print("Por favor, introduce un valor numérico para el precio.")
                else:
                    break

            while True:
                nueva_cantidad = input("Introduce la nueva cantidad (o deja en blanco para no cambiar): ")
                if nueva_cantidad:
                    try:
                        producto['cantidad'] = int(nueva_cantidad)
                        break
                    except ValueError:
                        print("Por favor, introduce un número entero para la cantidad.")
                else:
                    break

            print(f"Producto '{producto['nombre']}' actualizado exitosamente.\n")
            return
    print(f"Producto con nombre '{nombre}' no encontrado.\n")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado exitosamente.\n")
            return
    print(f"Producto con nombre '{nombre}' no encontrado.\n")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados exitosamente en productos.txt.\n")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
        print("Datos cargados exitosamente de productos.txt.\n")
    except FileNotFoundError:
        print("No se encontró el archivo productos.txt, comenzando con un inventario vacío.\n")

def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            anadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.\n")


menu()
