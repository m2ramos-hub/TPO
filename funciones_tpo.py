#Pro-Gamer Logistics
#Menu hecho por Lautaro Cordoba
#Inventario hecho por Esteban Jumilla
#Validaciones hechas por Manuel Dos Ramos y Juan Cruz Gallo

import random
# marcas_disponibles: catalogo de marcas 
# lista paralela 'marcas' del inventario).
marcas_disponibles = ["Logitech", "Razer", "Corsair", "Zowie", "ASUS", "HyperX"]
nombres_monitor  = ["Monitor 24 Full HD ", "Monitor 27 2K 144Hz", "Monitor 32 4K HDR", "Monitor 24 240Hz", "Monitor curvo 34 UltraWide"]
nombres_teclado  = ["Teclado mecanico TKL", "Teclado mecanico full-size RGB", "Teclado membrana compacto", "Teclado inalambrico Bluetooth", "Teclado gaming con wrist"]
nombres_mouse     = ["Mouse gaming 16000 DPI", "Mouse inalambrico ergonomico", "Mouse optico compacto", "Mouse ambidiestro 3360 sensor", "Mouse ultraligero honeycomb"]
nombres_microfono = ["Microfono USB cardioide", "Microfono condensador RGB", "Microfono XLR profesional", "Microfono de escritorio compacto"]
nombres_mousepad  = ["Mousepad XL de tela", "Mousepad rigido de aluminio", "Mousepad XXL escritorio completo", "Mousepad con carga inalambrica", "Mousepad mediano antideslizante"]
nombres_auricular = ["Auriculares gaming 7.1 surround", "Auriculares inalambricos 9,1", "Auriculares over-ear noise cancelling", "Headset USB compacto"]
nombres_cable     = ["Cable USB-A a USB-C 2m", "Cable HDMI 2.1 4K 3m", "Cable DisplayPort 1.4 2m", "Cable de red Cat6 5m", "Cable extension USB 3.0 1.5m", "Cable de audio 3.5mm 1m"]
nombres_accesorio = ["Hub USB 7 puertos", "Adaptador USB-C multipuerto", "Webcam Full HD 1080p", "Almohadilla reposamunyecas", "Soporte para auriculares", "Iluminacion LED escritorio"]
nombres_varios   = ["Soporte articulado para monitor", "Soporte doble monitor", "Soporte vertical para PC tower", "Soporte de escritorio ajustable", "Brazo VESA 17-32"]

todas_categorias = ["Monitor", "Teclado", "Mouse", "Microfono", "Mousepad", "Auriculares", "Cable", "Accesorio", "Soporte"]
todas_nombres = [nombres_monitor, nombres_teclado, nombres_mouse, nombres_microfono, nombres_mousepad, nombres_auricular, nombres_cable, nombres_accesorio, nombres_varios]

# BLOQUE 1 — Validaciones de Texto


def validar_id(id_texto):
    if len(id_texto) < 4 or len(id_texto) > 10:
        return False
    for caracter in id_texto:
        if not caracter.isalpha() and not caracter.isdigit() and caracter != "_":#isaplha=si todos los caracteres son letras/isdigit=si todos los caracteres son numeros
            return False
    return True


def validar_descripcion(descripcion):
    if len(descripcion) == 0:
        return False
    elif not descripcion[0].isalpha():
        return False
    else:
        return True


def validar_categoria(categoria):

    categoria = categoria.capitalize() #esta funcion convierte la primera letra en mayuscula y el resto en minusculas.
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


def id_existe(ids, id_candidato):
    # recorre la lista de ids y avisa si ya hay uno igual
    i = 0
    while i < len(ids):
        if ids[i] == id_candidato:
            return True
        i = i + 1
    return False


def buscar_indice_por_id(ids, id_buscado):
    i = 0
    while i < len(ids):
        if ids[i] == id_buscado:
            return i
        i = i + 1
    return -1


def buscar_indice_por_nombre(nombres, nombre_buscado):
    i = 0
    while i < len(nombres):
        if nombres[i].lower() == nombre_buscado.lower():
            return i
        i = i + 1
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


def generar_id(ids, categoria):
    """
    Genera un ID unico para un producto nuevo.
    Usa las primeras 3 letras de la categoria + 3 numeros aleatorios.
    Verifica que no exista un ID igual en la lista de ids antes de retornarlo.
    """
    letras = categoria[0] + categoria[1] + categoria[2]
    numeros = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    candidato = letras + numeros
    while id_existe(ids, candidato):
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



#  MOSTRAR INVENTARIO
def ordenar_inventario(ids, nombres, categorias, marcas, precios, stocks):
    # metodo de burbuja: compara elementos adyacentes y los intercambia.
    # ordena por stock descendente, desempate alfabetico por nombre.
    # cada intercambio se hace en las 6 listas
    # con el mismo indice para que no se desalineen.
    n = len(ids)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            cambiar = False
            if stocks[j] < stocks[j + 1]:
                
                cambiar = True
            elif stocks[j] == stocks[j + 1]:
                
                if nombres[j].lower() > nombres[j + 1].lower():
                    cambiar = True
            if cambiar:
                
                temp = ids[j]
                ids[j] = ids[j + 1]
                ids[j + 1] = temp

                temp = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = temp

                temp = categorias[j]
                categorias[j] = categorias[j + 1]
                categorias[j + 1] = temp

                temp = marcas[j]
                marcas[j] = marcas[j + 1]
                marcas[j + 1] = temp

                temp = precios[j]
                precios[j] = precios[j + 1]
                precios[j + 1] = temp

                temp = stocks[j]
                stocks[j] = stocks[j + 1]
                stocks[j + 1] = temp
            j = j + 1
        i = i + 1


def mostrar_inventario(ids, nombres, categorias, precios, stocks):
    if len(ids) == 0:
        print("\n  El inventario esta vacio.\n")
    else:
        print("\n" + "=" * 80)
        print("  " + "ID".ljust(10) + "PRODUCTO".ljust(50) + "CATEGORIA".ljust(13) + "PRECIO".rjust(10) + "STOCK".rjust(6))
        print("=" * 80)
        i = 0
        while i < len(ids):
            print("  " + str(ids[i]).ljust(10) + nombres[i].ljust(50) + categorias[i].ljust(13) + ("$" + str(precios[i])).rjust(10) + str(stocks[i]).rjust(6))
            i = i + 1
        print("=" * 80)
        print("  Total de productos: " + str(len(ids)) + "\n")


def informe_general(ids, nombres, categorias, marcas, precios, stocks):
    
    if len(ids) == 0:
        print("\n  El inventario esta vacio.\n")
    else:
        ordenar_inventario(ids, nombres, categorias, marcas, precios, stocks)
        mostrar_inventario(ids, nombres, categorias, precios, stocks)


#  AGREGAR PRODUCTO

def agregar_producto(ids, nombres, categorias, marcas, precios, stocks):
    print("\n-- AGREGAR PRODUCTO ---------------------")
    print("Categorias disponibles:")
    i = 0
    while i < len(todas_categorias):
        print("  " + str(i + 1) + ". " + todas_categorias[i])
        i = i + 1

    opcion_cat = input("Elegí una categoria (numero): ").strip()

    if not opcion_cat.isdigit() or int(opcion_cat) < 1 or int(opcion_cat) > len(todas_categorias):
        print("  Opcion invalida. Volvé al menu e intentá de nuevo.")
    else:
        idx_cat   = int(opcion_cat) - 1
        categoria = todas_categorias[idx_cat]#es el indice de la categoria seleccionada, es la posicion en la lista.
        nombres_cat = todas_nombres[idx_cat]#nombres del catalogo de esa categoria (no confundir con la lista paralela 'nombres')

        print("\nProductos en '" + categoria + "':")
        i = 0
        while i < len(nombres_cat):
            print("  " + str(i + 1) + ". " + nombres_cat[i])
            i = i + 1
        print("  " + str(len(nombres_cat) + 1) + ". Ingresar nombre personalizado")

        opcion_nom = input("Elegí el producto (numero): ").strip()

        if not opcion_nom.isdigit() or int(opcion_nom) < 1 or int(opcion_nom) > len(nombres_cat) + 1:
            print("  Opcion invalida. Volvé al menu e intentá de nuevo.")
        else:
            idx_nom = int(opcion_nom) - 1
            if idx_nom < len(nombres_cat):
                nombre_base = nombres_cat[idx_nom]
            else:
                nombre_base = input("Nombre del producto: ").strip()

            if not validar_descripcion(nombre_base):
               
                print("  El nombre no puede estar vacio y debe comenzar con una letra.")
            else:
                print("\nMarcas disponibles:")
                i = 0
                while i < len(marcas_disponibles):
                    print("  " + str(i + 1) + ". " + marcas_disponibles[i])
                    i = i + 1
                print("  " + str(len(marcas_disponibles) + 1) + ". Ingresar marca personalizada")

                opcion_marca = input("Elegí la marca (numero): ").strip()

                if not opcion_marca.isdigit() or int(opcion_marca) < 1 or int(opcion_marca) > len(marcas_disponibles) + 1:
                    print("  Opcion invalida. Volvé al menu e intentá de nuevo.")
                else:
                    idx_marca = int(opcion_marca) - 1
                    if idx_marca < len(marcas_disponibles):
                        marca = marcas_disponibles[idx_marca]
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
                            print("  Precio invalido.")
                        elif not validar_stock(stock_str):
                            print("  Stock invalido.")
                        else:
                            nuevo_nombre = marca + " " + nombre_base
                            if buscar_indice_por_nombre(nombres, nuevo_nombre) != -1:
                                print("  El producto '" + nuevo_nombre + "' ya existe en el inventario.")
                            else:
                                nuevo_id = generar_id(ids, categoria)
                                ids.append(nuevo_id)
                                nombres.append(nuevo_nombre)
                                categorias.append(categoria)
                                marcas.append(marca)
                                precios.append(float(precio_str))
                                stocks.append(int(stock_str))
                                print("  Producto '" + nuevo_nombre + "' agregado con ID " + str(nuevo_id) + ".\n")


#  ELIMINAR PRODUCTO



def eliminar_producto(ids, nombres, categorias, marcas, precios, stocks):
    print("\n-- ELIMINAR PRODUCTO --------------------")
    mostrar_inventario(ids, nombres, categorias, precios, stocks)
    if len(ids) > 0:
        id_str = input("ID del producto a eliminar (salir para cancelar): ").strip().capitalize()
        if id_str == "Salir":
            print("  Operacion cancelada.")
        else:
            indice = buscar_indice_por_id(ids, id_str)
            if indice == -1:
                print("  ID no encontrado.")
            else:
                if stocks[indice] > 0: 
                    print("  El producto tiene stock. No se puede eliminar.")
                else:
                    confirmar = input("  Eliminar '" + nombres[indice] + "'? (s/n): ").strip().lower()
                    if confirmar == "s":
                        ids.pop(indice)
                        nombres.pop(indice)
                        categorias.pop(indice)
                        marcas.pop(indice)
                        precios.pop(indice)
                        stocks.pop(indice)
                        print("  Producto eliminado.")
                    else:
                        print("  Operacion cancelada.")

# Modificar Stock

def modificar_stock(ids, nombres, categorias, precios, stocks):
    print("\n-- MODIFICAR STOCK ----------------------")
    mostrar_inventario(ids, nombres, categorias, precios, stocks)
    if len(ids) > 0:
        nombre_str = input("Nombre del producto (salir para cancelar): ").strip()
        # consigna: modificar busca por descripcion o nombre comercial, no por ID
        if nombre_str == "salir":
            print("  Operacion cancelada.")
        else:
            indice = buscar_indice_por_nombre(nombres, nombre_str)
            if indice == -1:
                print("  Producto no encontrado.")
            else:
                print("  Producto: " + nombres[indice])
                print("  Stock actual: " + str(stocks[indice]))
                print("  1. Sumar stock")
                print("  2. Restar stock")
                print("  3. Establecer stock exacto")
                op = input("  Opcion: ").strip()
                cantidad_str = input("  Cantidad: ").strip()

                if op not in ["1", "2", "3"]:
                    print("  Opcion invalida.")
                elif not cantidad_str.isdigit() or int(cantidad_str) < 0:
                    print("  Cantidad invalida.")
                elif op == "1":
                    stocks[indice] = stocks[indice] + int(cantidad_str)
                    print("  Stock actualizado: " + str(stocks[indice]) + " unidades.\n")
                elif op == "2":
                    if stocks[indice] - int(cantidad_str) < 0:
                        print("  Error: el stock no puede quedar negativo.")
                    else:
                        stocks[indice] = stocks[indice] - int(cantidad_str)
                        print("  Stock actualizado: " + str(stocks[indice]) + " unidades.\n")
                elif op == "3":
                    stocks[indice] = int(cantidad_str)
                    print("  Stock establecido en: " + str(int(cantidad_str)) + " unidades.\n")


#  MODIFICAR PRECIO

def modificar_precio(ids, nombres, categorias, precios, stocks):
    print("\n-- MODIFICAR PRECIO ---------------------")
    mostrar_inventario(ids, nombres, categorias, precios, stocks)
    if len(ids) > 0:
        #Puse el capitalize porque cuando se ingresaba el ID sin la mayuscula se devolvia al menu principal
        id_str = input("ID del producto (salir para cancelar): ").strip().capitalize()
        if id_str == "Salir":
            print("  Operacion cancelada.")
        else:
            indice = buscar_indice_por_id(ids, id_str)
            if indice == -1:
                print("  ID no encontrado.")
            else:
                print("  Producto: " + nombres[indice])
                print("  Precio actual: $" + str(precios[indice]))
                precio_str = input("  Nuevo precio ($): ").strip()
                if not es_numero_decimal(precio_str) or float(precio_str) < 0:
                    print("  Precio invalido.")
                else:
                    precios[indice] = float(precio_str)
                    print("  Precio actualizado a $" + precio_str + ".\n")


#  BUSCAR PRODUCTO

def buscar_producto(ids, nombres, categorias, marcas, precios, stocks):
    print("\n-- BUSCAR PRODUCTO ----------------------")
    termino = input("Nombre, categoria o marca: ").strip().lower()
    res_ids = []
    res_nombres = []
    res_categorias = []
    res_precios = []
    res_stocks = []
    i = 0
    while i < len(ids):
        if termino in nombres[i].lower() or termino in categorias[i].lower() or termino in marcas[i].lower():
            res_ids.append(ids[i])
            res_nombres.append(nombres[i])
            res_categorias.append(categorias[i])
            res_precios.append(precios[i])
            res_stocks.append(stocks[i])
        i = i + 1
    if len(res_ids) == 0:
        print("  No se encontraron productos con '" + termino + "'.\n")
    else:
        mostrar_inventario(res_ids, res_nombres, res_categorias, res_precios, res_stocks)


#  MENU PRINCIPAL

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
