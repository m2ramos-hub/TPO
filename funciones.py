import random
marcas = ["Logitech", "Razer", "Corsair", "Zowie", "ASUS", "HyperX"]
nombres_monitor  = ["Monitor 24 Full HD ", "Monitor 27 2K 144Hz", "Monitor 32 4K HDR", "Monitor 24 240Hz", "Monitor curvo 34 UltraWide"]
nombres_teclado  = ["Teclado mecanico TKL", "Teclado mecanico full-size RGB", "Teclado membrana compacto", "Teclado inalambrico Bluetooth", "Teclado gaming con wrist"]
nombres_mouse     = ["Mouse gaming 16000 DPI", "Mouse inalambrico ergonomico", "Mouse optico compacto", "Mouse ambidiestro 3360 sensor", "Mouse ultraligero honeycomb"]
nombres_microfono = ["Microfono USB cardioide", "Microfono condensador RGB", "Microfono XLR profesional", "Microfono de escritorio compacto"]
nombres_mousepad  = ["Mousepad XL de tela", "Mousepad rigido de aluminio", "Mousepad XXL escritorio completo", "Mousepad con carga inalambrica", "Mousepad mediano antideslizante"]
nombres_auricular = ["Auriculares gaming 7.1 surround", "Auriculares inalambricos 9,1", "Auriculares over-ear noise cancelling", "Headset USB compacto"]
nombres_cable     = ["Cable USB-A a USB-C 2m", "Cable HDMI 2.1 4K 3m", "Cable DisplayPort 1.4 2m", "Cable de red Cat6 5m", "Cable extension USB 3.0 1.5m", "Cable de audio 3.5mm 1m"]
nombres_accesorio = ["Hub USB 7 puertos", "Adaptador USB-C multipuerto", "Webcam Full HD 1080p", "Almohadilla reposamunyecas", "Soporte para auriculares", "Iluminacion LED escritorio"]
nombres_varios   = ["Soporte articulado para monitor", "Soporte doble monitor", "Soporte vertical para PC tower", "Soporte de escritorio ajustable", "Brazo VESA 17-32"]

todas_categorias= ["Monitor", "Teclado", "Mouse", "Microfono", "Mousepad", "Auriculares", "Cable", "Accesorio", "Soporte"]
todas_nombres = [nombres_monitor, nombres_teclado, nombres_mouse, nombres_microfono, nombres_mousepad, nombres_auricular, nombres_cable, nombres_accesorio, nombres_varios]


# BLOQUE 1 — Validaciones de Texto 


def validar_id(id_texto):
    if len(id_texto) < 4 or len(id_texto) > 10:
        return False
    for caracter in id_texto:
        if not caracter.isalpha() and not caracter.isdigit() and caracter != "_":#isaplha=si todos los caracteres son letras/isdigit=si todos los caracteres son numeros
            return False
    return True


def validacion_id_duplicado(inventario, id):
    for j in inventario:
        if id == j:
            return True
    return False


def validar_descripcion(descripcion):   
    if len(descripcion) == 0:
        return False
    elif not descripcion[0].isalpha():
        return False
    else:
        return True


def validar_categoria(categoria):

    categoria=categoria.capitalize() #esta funcion  convierte la primera letra en mayúscula y el resto en minúsculas.
    #fuente:https://docs.python.org/3/library/stdtypes.html#str.capitalize
    for cat in todas_categorias:
        if cat == categoria:
            return categoria
    return "Varios"


def validar_marca(marca):

    if len(marca) == 0 or len(marca) < 3:
        return False
    for j in marca:
        if not j.isalpha() and not j == " ":
            return False
    return True


def id_existe(inventario, id_candidato):
    i = 0
    while i < len(inventario):
        if inventario[i]["id"] == id_candidato:
            return True
        i = i + 1
    return False


def buscar_indice_por_id(inventario, id_buscado):
    i = 0
    while i < len(inventario):
        if inventario[i]["id"] == id_buscado:
            return i
        i = i + 1
    return -1


def buscar_indice_por_nombre(inventario, nombre_buscado):
    for i in range(len(inventario)):
        if inventario[i]["nombre"].lower() == nombre_buscado.lower():
            return i
    return -1


# BLOQUE 2 — Validaciones Numericas


def es_numero_entero(texto):
    """
    Verifica si un texto representa un numero entero.
    Recorre caracter por caracter comparando contra '0' y '9'.
    Acepta numeros negativos con '-' al inicio.
    Retorna True si todos los caracteres son digitos, False en caso contrario.
    """
    if len(texto) == 0:
        return False
    inicio = 0
    if texto[0] == "-":
        inicio = 1
    if inicio == len(texto):
        return False
    i = inicio
    while i < len(texto):
        if texto[i] < "0" or texto[i] > "9":
            return False
        i = i + 1
    return True


def es_numero_decimal(texto):
    """
    Verifica si un texto representa un numero decimal (float).
    Acepta un unico punto '.' como separador decimal.
    Acepta numeros negativos con '-' al inicio.
    Retorna True si el texto es un numero decimal valido, False en caso contrario.
    """
    if len(texto) == 0:
        return False
    puntos = 0
    digitos = 0
    inicio = 0
    if texto[0] == "-":
        inicio = 1
    if inicio == len(texto):
        return False
    i = inicio
    while i < len(texto):
        if texto[i] == ".":
            puntos = puntos + 1
            if puntos > 1:
                return False
        elif texto[i] < "0" or texto[i] > "9":
            return False
        else:
            digitos = digitos + 1
        i = i + 1
    return digitos > 0


def validar_precio(precio_str):
    """
    Valida que el precio ingresado sea un numero decimal positivo.
    Retorna True si el precio es valido (mayor a 0), False en caso contrario.
    """
    if not es_numero_decimal(precio_str):
        return False
    if float(precio_str) <= 0:
        return False
    return True


def validar_stock(stock_str):
    """
    Valida que el stock ingresado sea un numero entero positivo.
    Retorna True si el stock es valido (mayor o igual a 1), False en caso contrario.
    """
    if not es_numero_entero(stock_str):
        return False
    if int(stock_str) < 1:
        return False
    return True


def generar_id(inventario, categoria):
    """
    Genera un ID unico para un producto nuevo.
    Usa las primeras 3 letras de la categoria + 3 numeros aleatorios.
    Verifica que no exista un ID igual en el inventario antes de retornarlo.
    """
    letras = categoria[0] + categoria[1] + categoria[2]
    numeros = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    candidato = letras + numeros
    while id_existe(inventario, candidato):
        numeros = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        candidato = letras + numeros
    return candidato


def indice_categoria(categoria):
    """
    Busca y retorna el indice de una categoria en todas_categorias.
    Retorna -1 si la categoria no existe.
    """
    i = 0
    while i < len(todas_categorias):
        if todas_categorias[i] == categoria:
            return i
        i = i + 1
    return -1


# ─────────────────────────────────────────
#  MOSTRAR INVENTARIO
# ─────────────────────────────────────────


def ordenar_inventario(inventario):
    # metodo de burbuja: compara elementos adyacentes y los intercambia
    # ordena por stock descendente, desempate alfabetico por nombre
    n = len(inventario)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            cambiar = False
            if inventario[j]["stock"] < inventario[j + 1]["stock"]:
                # stock menor a la izquierda, hay que intercambiar
                cambiar = True
            elif inventario[j]["stock"] == inventario[j + 1]["stock"]:
                # empate de stock, desempate alfabetico
                if inventario[j]["nombre"].lower() > inventario[j + 1]["nombre"].lower():
                    cambiar = True
            if cambiar:
                # intercambio con variable temporal
                temp = inventario[j]
                inventario[j] = inventario[j + 1]
                inventario[j + 1] = temp
            j = j + 1
        i = i + 1


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("\n  El inventario esta vacio.\n")
    else:
        print("\n" + "=" * 80)
        print("  " + "ID".ljust(10) + "PRODUCTO".ljust(50) + "CATEGORIA".ljust(13) + "PRECIO".rjust(10) + "STOCK".rjust(6))
        print("=" * 80)
        i = 0
        while i < len(inventario):
            p = inventario[i]
            print("  " + str(p["id"]).ljust(10) + p["nombre"].ljust(50) + p["categoria"].ljust(13) + ("$" + str(p["precio"])).rjust(10) + str(p["stock"]).rjust(6))
            i = i + 1
        print("=" * 80)
        print("  Total de productos: " + str(len(inventario)) + "\n")


def informe_general(inventario):
    # muestra productos ordenados por stock desc, desempate alfabetico
    if len(inventario) == 0:
        print("\n  El inventario esta vacio.\n")
    else:
        ordenar_inventario(inventario)
        mostrar_inventario(inventario)
# ─────────────────────────────────────────
#  AGREGAR PRODUCTO
# ─────────────────────────────────────────


def agregar_producto(inventario):
    print("\n-- AGREGAR PRODUCTO ---------------------")
    print("Categorias disponibles:")
    i = 0
    while i < len(todas_categorias):
        print("  " + str(i + 1) + ". " + todas_categorias[i])
        i = i + 1

    opcion_cat = input("Elegí una categoria (numero): ").strip()

    if not opcion_cat.isdigit() or int(opcion_cat) < 1 or int(opcion_cat) > len(todas_categorias):
        #se realizo cambio de estructura para que coincida con validaciones
        print("  Opcion invalida. Volvé al menu e intentá de nuevo.")
    else:
        idx_cat   = int(opcion_cat) - 1
        categoria = todas_categorias[idx_cat]#es el índice de la categoría seleccionada, es la posición en la lista.
        nombres   = todas_nombres[idx_cat]

        print("\nProductos en '" + categoria + "':")
        i = 0
        while i < len(nombres):
            print("  " + str(i + 1) + ". " + nombres[i])
            i = i + 1
        print("  " + str(len(nombres) + 1) + ". Ingresar nombre personalizado")

        opcion_nom = input("Elegí el producto (numero): ").strip()

        if not opcion_nom.isdigit() or int(opcion_nom) < 1 or int(opcion_nom) > len(nombres) + 1:
            #se realizo cambio de estructura para que coincida con validaciones
            print("  Opcion invalida. Volvé al menu e intentá de nuevo.")
        else:
            idx_nom = int(opcion_nom) - 1
            if idx_nom < len(nombres):
                nombre_base = nombres[idx_nom]
            else:
                nombre_base = input("Nombre del producto: ").strip()

            if not validar_descripcion(nombre_base):
                # se llama validar_descripcion() — verifica que no este vacio
                # y que el primer caracter sea una letra
                print("  El nombre no puede estar vacio y debe comenzar con una letra.")
            else:
                print("\nMarcas disponibles:")
                i = 0
                while i < len(marcas):
                    print("  " + str(i + 1) + ". " + marcas[i])
                    i = i + 1
                print("  " + str(len(marcas) + 1) + ". Ingresar marca personalizada")

                opcion_marca = input("Elegí la marca (numero): ").strip()

                if not opcion_marca.isdigit() or int(opcion_marca) < 1 or int(opcion_marca) > len(marcas) + 1:
                    #se realizo cambio de estructura para que coincida con validaciones
                    print("  Opcion invalida. Volvé al menu e intentá de nuevo.")
                else:
                    idx_marca = int(opcion_marca) - 1
                    if idx_marca < len(marcas):
                        marca = marcas[idx_marca]
                    else:
                        marca = input("Nombre de la marca: ").strip()

                    if not validar_marca(marca):
                    # se llama validar_marca() — verifica que no este vacia,
                    # tenga al menos 3 letras y contenga solo letras y espacios
                        print("  Marca invalida. Debe tener al menos 3 letras y solo letras.")
                    else:
                        precio_str = input("Precio ($): ").strip()
                        stock_str  = input("Stock inicial: ").strip()

                        if not validar_precio(precio_str):
                            # se llama validar_precio() — reemplaza el replace().isdigit() manual,
                            # verifica que sea decimal y estrictamente positivo (mayor a 0)
                            print("  Precio invalido.")
                        elif not validar_stock(stock_str):
                            # se llama validar_stock() — reemplaza el isdigit() manual,
                            # verifica que sea entero y mayor o igual a 1
                            print("  Stock invalido.")
                            #se realizo cambio de estructura para que coincida con validaciones.
                        else:
                            nuevo = {
                                "id":        generar_id(inventario, categoria),
                                "nombre":    marca + " " + nombre_base,
                                "categoria": categoria,
                                "marca":     marca,
                                "precio":    float(precio_str),
                                "stock":     int(stock_str),
                            }
                            inventario.append(nuevo)
                            print("  Producto '" + nuevo["nombre"] + "' agregado con ID " + str(nuevo["id"]) + ".\n")

# ─────────────────────────────────────────
#  ELIMINAR PRODUCTO
# ─────────────────────────────────────────


def eliminar_producto(inventario):
    print("\n-- ELIMINAR PRODUCTO --------------------")
    mostrar_inventario(inventario)
    if len(inventario) > 0:
        id_str = input("ID del producto a eliminar (salir para cancelar): ").strip().capitalize()
        if id_str == "Salir":
            print("  Operacion cancelada.")
        else:
            indice = buscar_indice_por_id(inventario, id_str)
            if indice == -1:
                print("  ID no encontrado.")
            else:
                if inventario[indice]["stock"] > 0:
                    # solo se puede eliminar si stock es igual a 0
                    # si tiene stock disponible, se informa y se cancela
                    # no se puede eliminar si tiene stock
                    print("  El producto tiene stock. No se puede eliminar.")
                else:
                    # stock es 0, se solicita confirmacion antes de eliminar
                    confirmar = input("  Eliminar '" + inventario[indice]["nombre"] + "'? (s/n): ").strip().lower()
                    if confirmar == "s":
                        inventario.pop(indice)
                        print("  Producto eliminado.")
                    else:
                        # el usuario cancelo la operacion
                        print("  Operacion cancelada.")

# ─────────────────────────────────────────
#  MODIFICAR STOCK
# ─────────────────────────────────────────


def modificar_stock(inventario):
    print("\n-- MODIFICAR STOCK ----------------------")
    mostrar_inventario(inventario)
    if len(inventario) > 0:
        nombre_str = input("Nombre del producto (salir para cancelar): ").strip()
        # consigna: modificar busca por descripcion o nombre comercial, no por ID
        if nombre_str == "salir":
            print("  Operacion cancelada.")
        else:
            indice = buscar_indice_por_nombre(inventario, nombre_str)
            if indice == -1:
                print("  Producto no encontrado.")
            else:
                p = inventario[indice]
                print("  Producto: " + p["nombre"])
                print("  Stock actual: " + str(p["stock"]))
                print("  1. Sumar stock")
                print("  2. Restar stock")
                print("  3. Establecer stock exacto")
                op = input("  Opcion: ").strip()
                cantidad_str = input("  Cantidad: ").strip()

                if op not in ["1", "2", "3"]:
                    print("  Opcion invalida.")
                elif not cantidad_str.isdigit() or int(cantidad_str) < 0:
                    print("  Cantidad invalida.")  # se realizo cambio de estructura para que coincida con validaciones
                elif op == "1":
                    inventario[indice]["stock"] = p["stock"] + int(cantidad_str)
                    print("  Stock actualizado: " + str(inventario[indice]["stock"]) + " unidades.\n")
                elif op == "2":
                    if p["stock"] - int(cantidad_str) < 0:
                        print("  Error: el stock no puede quedar negativo.")
                    else:
                        inventario[indice]["stock"] = p["stock"] - int(cantidad_str)
                        print("  Stock actualizado: " + str(inventario[indice]["stock"]) + " unidades.\n")
                elif op == "3":
                    inventario[indice]["stock"] = int(cantidad_str)
                    print("  Stock establecido en: " + str(int(cantidad_str)) + " unidades.\n")

# ─────────────────────────────────────────
#  MODIFICAR PRECIO
# ─────────────────────────────────────────


def modificar_precio(inventario):
    print("\n-- MODIFICAR PRECIO ---------------------")
    mostrar_inventario(inventario)
    if len(inventario) > 0:
        #Puse el capitalize porque cuando se ingresaba el ID sin la mayuscula se devolvia al menu principal
        id_str = input("ID del producto (salir para cancelar): ").strip().capitalize()
        if id_str == "salir":
            print("  Operacion cancelada.")
        else:
            indice = buscar_indice_por_id(inventario, id_str)
            if indice == -1:
                print("  ID no encontrado.")
            else:
                print("  Producto: " + inventario[indice]["nombre"])
                print("  Precio actual: $" + str(inventario[indice]["precio"]))
                precio_str = input("  Nuevo precio ($): ").strip()
                if not es_numero_decimal(precio_str) or float(precio_str) < 0:
                    print("  Precio invalido.")
                else:
                    inventario[indice]["precio"] = float(precio_str)
                    print("  Precio actualizado a $" + precio_str + ".\n")

# ─────────────────────────────────────────
#  BUSCAR PRODUCTO
# ─────────────────────────────────────────


def buscar_producto(inventario):
    print("\n-- BUSCAR PRODUCTO ----------------------")
    termino = input("Nombre, categoria o marca: ").strip().lower()
    resultados = []
    i = 0
    while i < len(inventario):
        p = inventario[i]
        if termino in p["nombre"].lower() or termino in p["categoria"].lower() or termino in p["marca"].lower():
            resultados.append(p)
        i = i + 1
    if len(resultados) == 0:
        print("  No se encontraron productos con '" + termino + "'.\n")
    else:
        mostrar_inventario(resultados)

# ─────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────

def mostrar_menu():
    '''se cambio para que coincida con la consigna, y unificando procesos'''
    print("\n" + "=" * 50)
    print("   SISTEMA DE GESTION: STOCK-GAMER")
    print("=" * 50)
    print("  1. Registrar nuevo producto (Alta)")
    print("  2. Eliminar producto del sistema (Baja)")
    print("  3. Modificar cantidad en stock (Modificacion)")
    print("  4. Informe General - Visualizacion de los datos")
    print("  8. Salir")
    print("=" * 50)
