import random

# Colores (capa visual)
rojo = "\033[31m"
verde = "\033[32m"
blanco = "\033[0m"


def procesar_y_buscar_id(ids, id_ingresado):
    """
    FUNCION UNIFICADA DE ID
    Usa un ciclo for-else para verificar caracteres sin banderas.
    Usa un while puro combinando condiciones logicas para la busqueda.
    """
    indice_resultado = -1
    if len(id_ingresado) >= 4 and len(id_ingresado) <= 10:
        for caracter in id_ingresado:
            if not caracter.isalpha() and not caracter.isdigit() and caracter != "_":
                break
        else:
            # for-else: el else corre solo si el for termino sin break
            i = 0
            largo_lista = len(ids)
            while i < largo_lista and indice_resultado == -1:
                if ids[i] == id_ingresado:
                    indice_resultado = i
                i = i + 1
    return indice_resultado


def generar_id(ids, categoria):
    """
    Genera un ID unico: primeras 3 letras de la categoria + 3 numeros al azar.
    Repite la generacion mientras el ID ya exista.
    """
    letras = categoria[0] + categoria[1] + categoria[2]
    numeros = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    candidato = letras + numeros
    while procesar_y_buscar_id(ids, candidato) != -1:
        numeros = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
        candidato = letras + numeros
    return candidato


def validar_descripcion(descripcion):
    if len(descripcion) == 0:
        return False
    elif not descripcion[0].isalpha():
        return False
    else:
        return True


def validar_categoria(categoria, todas_categorias):
    categoria = categoria.capitalize()
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


def buscar_indice_por_nombre(nombres, nombre_buscado):
    i = 0
    while i < len(nombres):
        if nombres[i].lower() == nombre_buscado.lower():
            return i
        i = i + 1
    return -1


def producto_duplicado(nombres, categorias, marcas, nombre, categoria, marca):
    """
    RF01: indica si ya existe un producto con la misma combinacion
    nombre + categoria + marca, aunque el ID sea distinto. Ciclo puro, sin bandera.
    """
    encontrado = -1
    i = 0
    while i < len(nombres) and encontrado == -1:
        if nombres[i].lower() == nombre.lower() and categorias[i] == categoria and marcas[i].lower() == marca.lower():
            encontrado = i
        i = i + 1
    return encontrado != -1


def nombre_existe_en_catalogo(todas_nombres, nombre):
    """
    RF08: indica si un nombre ya existe en cualquier categoria del catalogo.
    Reutiliza buscar_indice_por_nombre. Ciclo puro, sin bandera.
    """
    encontrado = -1
    i = 0
    while i < len(todas_nombres) and encontrado == -1:
        if buscar_indice_por_nombre(todas_nombres[i], nombre) != -1:
            encontrado = i
        i = i + 1
    return encontrado != -1


# BLOQUE 2 — Validaciones Numericas

def es_numero_entero(texto):
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
    puntos = 0
    digitos = 0
    inicio = 0
    if len(texto) > 0 and texto[0] == "-":
        inicio = 1
    i = inicio
    while i < len(texto):
        if texto[i] == ".":
            puntos = puntos + 1
            if puntos > 1:
                break
        elif texto[i] < "0" or texto[i] > "9":
            break
        else:
            digitos = digitos + 1
        i = i + 1
    return len(texto) > 0 and inicio < len(texto) and i == len(texto) and digitos > 0


def validar_precio(precio_str):
    if not es_numero_decimal(precio_str):
        return False
    if float(precio_str) <= 0:
        return False
    return True


def validar_stock(stock_str):
    if not es_numero_entero(stock_str):
        return False
    if int(stock_str) < 1:
        return False
    return True


def indice_categoria(categoria, todas_categorias):
    """
    Busca el indice de una categoria. posicion arranca en -1; si la encuentra la
    guarda y ROMPE EL CICLO con break (no la funcion). Unico return al final.
    """
    posicion = -1
    i = 0
    while i < len(todas_categorias):
        if todas_categorias[i] == categoria:
            posicion = i
            break
        i = i + 1
    return posicion


def mostrar_listado(lista_opciones, mensaje_peticion):
    """
    Muestra opciones numeradas, pide un numero, valida que exista en la lista y
    devuelve el texto de la opcion elegida. Si se equivoca, avisa y vuelve a pedir.
    """
    opcion_seleccionada = ""
    while opcion_seleccionada == "":
        print("\n Opciones disponibles:")
        for i in range(len(lista_opciones)):
            print("  " + str(i + 1) + ". " + lista_opciones[i])
        ingreso = input(mensaje_peticion)
        if ingreso.isdigit():
            indice = int(ingreso) - 1
            if 0 <= indice < len(lista_opciones):
                opcion_seleccionada = lista_opciones[indice]
        if opcion_seleccionada == "":
            print(rojo + "  [ERROR] Seleccion invalida. Ingrese un numero de la lista." + blanco)
    return opcion_seleccionada


def calcular_vuelto(monto):
    """
    RF07: muestra el vuelto con la menor cantidad de billetes posible (greedy,
    de mayor a menor).
    """
    billetes = [100,50,20,10,5,1]
    restante = int(monto)
    print("  Vuelto con la menor cantidad de billetes:")
    i = 0
    while i < len(billetes):
        cantidad = restante // billetes[i]
        if cantidad > 0:
            print("    " + str(cantidad) + " billete(s) de $" + str(billetes[i]))
            restante = restante - cantidad * billetes[i]
        i = i + 1


#  MOSTRAR / ORDENAR INVENTARIO
def ordenar_inventario(ids, nombres, categorias, marcas, precios, stocks, stock_minimo):
    # metodo de burbuja por stock descendente, desempate alfabetico por nombre.
    # cada intercambio se hace en las 7 listas con el mismo indice (RT02: sin bandera).
    n = len(ids)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if (stocks[j] < stocks[j + 1]) or (stocks[j] == stocks[j + 1] and nombres[j].lower() > nombres[j + 1].lower()):
                temp = ids[j]; ids[j] = ids[j + 1]; ids[j + 1] = temp
                temp = nombres[j]; nombres[j] = nombres[j + 1]; nombres[j + 1] = temp
                temp = categorias[j]; categorias[j] = categorias[j + 1]; categorias[j + 1] = temp
                temp = marcas[j]; marcas[j] = marcas[j + 1]; marcas[j + 1] = temp
                temp = precios[j]; precios[j] = precios[j + 1]; precios[j + 1] = temp
                temp = stocks[j]; stocks[j] = stocks[j + 1]; stocks[j + 1] = temp
                temp = stock_minimo[j]; stock_minimo[j] = stock_minimo[j + 1]; stock_minimo[j + 1] = temp
            j = j + 1
        i = i + 1

def exportar_csv(ids, nombres, categorias, precios, stocks, stock_minimo):
    '''RF05: genera un archivo CSV (separador punto y coma) con los productos
    que requieren reposicion (stock <= stock minimo).'''
    nombre_archivo = "reposicion.csv"
    archivo = open(nombre_archivo, "w")
    archivo.write("ID;PRODUCTO;CATEGORIA;PRECIO;STOCK;STOCK_MINIMO\n")
    cantidad = 0
    i = 0
    while i < len(ids):
        if stocks[i] <= stock_minimo[i]:
            linea = str(ids[i]) + ";" + nombres[i] + ";" + categorias[i] + ";" + str(precios[i]) + ";" + str(stocks[i]) + ";" + str(stock_minimo[i]) + "\n"
            archivo.write(linea)
            cantidad = cantidad + 1
        i = i + 1
    archivo.close()
    print(verde + "  Archivo '" + nombre_archivo + "' generado con " + str(cantidad) + " producto(s) para reponer." + blanco)

# MENUS (capa de presentacion)
def mostrar_menu():
    print(verde + "\n" + "=" * 50)
    print("   SISTEMA DE GESTION: PRO-GAMER LOGISTICS")
    print("=" * 50 + blanco)
    print("  1. Gestion de productos (Alta / Baja / Modificar)")
    print("  2. Registrar venta")
    print("  3. Informe general")
    print("  4. Configurar stock minimo")
    print("  5. Gestionar catalogo (ABM)")
    print("  6. Salir")
    print(verde + "=" * 50 + blanco)


def menu_gestion():
    print(verde + "\n-- GESTION DE PRODUCTOS ------------------" + blanco)
    print("  1. Alta de producto")
    print("  2. Baja de producto")
    print("  3. Modificar (stock / precio)")
    print("  4. Volver al menu principal")


def menu_modificar():
    print(verde + "\n-- MODIFICAR -----------------------------" + blanco)
    print("  1. Modificar stock")
    print("  2. Modificar precio")
    print("  3. Volver")


def menu_agregar_producto(todas_categorias):
    print(verde + "\n-- AGREGAR PRODUCTO ----------------------" + blanco)
    print("Elegi una categoria (o la ultima opcion para volver al menu):")
    return "Volver al menu principal"


# MAIN DE PRUEBA DEL MODULO (RT05)
def prueba():
    print("== Prueba de auxiliar_final ==")
    print("procesar_y_buscar_id(['Tec752'],'Tec752'):", procesar_y_buscar_id(["Tec752"], "Tec752"))
    print("procesar_y_buscar_id(['Tec752'],'Xxx999'):", procesar_y_buscar_id(["Tec752"], "Xxx999"))
    print("es_numero_decimal('12.5'):", es_numero_decimal("12.5"))
    print("es_numero_decimal('12..5'):", es_numero_decimal("12..5"))
    print("indice_categoria('Mouse',['Monitor','Mouse']):", indice_categoria("Mouse", ["Monitor", "Mouse"]))
    print("producto_duplicado:", producto_duplicado(["Logitech Mouse"], ["Mouse"], ["Logitech"], "Logitech Mouse", "Mouse", "Logitech"))
    calcular_vuelto(160)


if __name__ == "__main__":
    prueba()
