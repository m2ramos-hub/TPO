#Pro-Gamer Logistics
#Menu hecho por Lautaro Cordoba
#Inventario hecho por Esteban Jumilla
#Validaciones hechas por Manuel Dos Ramos y Juan Cruz Gallo

import auxiliar_f2 as aux

# Colores
rojo = "\033[31m"
verde = "\033[32m"
blanco = "\033[0m"


def crear_catalogo():
    """
    Crea el catalogo (RT07: sin variables globales). Retorna 3 listas:
    todas_categorias, todas_nombres (lista de listas alineada con categorias) y
    marcas_disponibles. Se llama una sola vez al inicio del programa.
    """
    marcas_disponibles = ["Logitech", "Razer", "Corsair", "Zowie", "ASUS", "HyperX"]
    nombres_monitor  = ["Monitor 24 Full HD", "Monitor 27 2K 144Hz", "Monitor 32 4K HDR", "Monitor 24 240Hz", "Monitor curvo 34 UltraWide"]
    nombres_teclado  = ["Teclado mecanico TKL", "Teclado mecanico full-size RGB", "Teclado membrana compacto", "Teclado inalambrico Bluetooth", "Teclado gaming con wrist"]
    nombres_mouse     = ["Mouse gaming 16000 DPI", "Mouse inalambrico ergonomico", "Mouse optico compacto", "Mouse ambidiestro 3360 sensor", "Mouse ultraligero honeycomb"]
    nombres_microfono = ["Microfono USB cardioide", "Microfono condensador RGB", "Microfono XLR profesional", "Microfono de escritorio compacto"]
    nombres_mousepad  = ["Mousepad XL de tela", "Mousepad rigido de aluminio", "Mousepad XXL escritorio completo", "Mousepad con carga inalambrica", "Mousepad mediano antideslizante"]
    nombres_auricular = ["Auriculares gaming 7.1 surround", "Auriculares inalambricos 9.1", "Auriculares over-ear noise cancelling", "Headset USB compacto"]
    nombres_cable     = ["Cable USB-A a USB-C 2m", "Cable HDMI 2.1 4K 3m", "Cable DisplayPort 1.4 2m", "Cable de red Cat6 5m", "Cable extension USB 3.0 1.5m", "Cable de audio 3.5mm 1m"]
    nombres_accesorio = ["Hub USB 7 puertos", "Adaptador USB-C multipuerto", "Webcam Full HD 1080p", "Almohadilla reposamunyecas", "Soporte para auriculares", "Iluminacion LED escritorio"]
    nombres_varios   = ["Soporte articulado para monitor", "Soporte doble monitor", "Soporte vertical para PC tower", "Soporte de escritorio ajustable", "Brazo VESA 17-32"]

    todas_categorias = ["Monitor", "Teclado", "Mouse", "Microfono", "Mousepad", "Auriculares", "Cable", "Accesorio", "Soporte"]
    todas_nombres = [nombres_monitor, nombres_teclado, nombres_mouse, nombres_microfono, nombres_mousepad, nombres_auricular, nombres_cable, nombres_accesorio, nombres_varios]
    return todas_categorias, todas_nombres, marcas_disponibles


# PRINCIPAL

def mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo):
    '''Muestra el inventario en tabla (incluye columna MIN del stock minimo, RF04).'''
    if len(ids) == 0:
        print(rojo + "\n  El inventario esta vacio.\n" + blanco)
    else:
        print(verde + "\n" + "=" * 86)
        print("  " + "ID".ljust(10) + "PRODUCTO".ljust(50) + "CATEGORIA".ljust(13) + "PRECIO".rjust(11) + "STOCK".rjust(7) + "MIN".rjust(5))
        print("=" * 86 + blanco)
        i = 0
        while i < len(ids):
            print("  " + str(ids[i]).ljust(10) + nombres[i].ljust(50) + categorias[i].ljust(13) + ("$" + str(precios[i])).rjust(11) + str(stocks[i]).rjust(7) + str(stock_minimo[i]).rjust(5))
            i = i + 1
        print(verde + "=" * 86 + blanco)
        print("  Total de productos: " + str(len(ids)) + "\n")


def informe_general(ids, nombres, categorias, marcas, precios, stocks, stock_minimo):
    '''Ordena y muestra el inventario y al final informa cuantos productos
    requieren reposicion (stock <= minimo) y su porcentaje (RF04).'''
    if len(ids) == 0:
        print(rojo + "\n  El inventario esta vacio.\n" + blanco)
    else:
        aux.ordenar_inventario(ids, nombres, categorias, marcas, precios, stocks, stock_minimo)
        mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
        necesitan = 0
        i = 0
        while i < len(ids):
            if stocks[i] <= stock_minimo[i]:
                necesitan = necesitan + 1
            i = i + 1
        porcentaje = necesitan * 100 / len(ids)
        print("  Productos que requieren reposicion: " + str(necesitan))
        print("  Porcentaje sobre el total: " + ("%.2f" % porcentaje) + "%\n")
        
        # RF05: consultar si desea exportar a CSV los productos que requieren reposicion
    opcion = input("  Desea exportar los productos que requieren reposicion a CSV? (si/no): ").lower()
    if opcion == "si":
        aux.exportar_csv(ids, nombres, categorias, precios, stocks, stock_minimo)



#  AGREGAR PRODUCTO

def agregar_producto(ids, nombres, categorias, marcas, precios, stocks, stock_minimo, todas_categorias, todas_nombres, marcas_disponibles):
    cant_salir = aux.menu_agregar_producto(todas_categorias)
    categoria = aux.mostrar_listado(todas_categorias + [cant_salir], "Elegi una opcion (numero): ")

    while categoria != cant_salir:
        idx_cat = todas_categorias.index(categoria)
        nombres_cat = todas_nombres[idx_cat]
        print("\nProductos en '" + categoria + "':")
        nombre_base = aux.mostrar_listado(nombres_cat, "Elegi el producto (numero): ")
        print("\nMarcas disponibles:")
        marca = aux.mostrar_listado(marcas_disponibles, "Elegi la marca (numero): ")

        precio_str = input("Precio ($): ")
        stock_str  = input("Stock inicial: ")

        if not aux.validar_precio(precio_str):
            print(rojo + "  Precio invalido." + blanco)
        elif not aux.validar_stock(stock_str):
            print(rojo + "  Stock invalido." + blanco)
        else:
            nuevo_nombre = marca + " " + nombre_base
            # RF01: no duplicar por marca + nombre + categoria
            if aux.producto_duplicado(nombres, categorias, marcas, nuevo_nombre, categoria, marca):
                print(rojo + "  Ya existe un producto con esa marca + nombre + categoria." + blanco)
            else:
                nuevo_id = aux.generar_id(ids, categoria)
                ids.append(nuevo_id)
                nombres.append(nuevo_nombre)
                categorias.append(categoria)
                marcas.append(marca)
                precios.append(float(precio_str))
                stocks.append(int(stock_str))
                stock_minimo.append(0)
                print("  Producto '" + nuevo_nombre + "' agregado con ID " + str(nuevo_id) + ".\n")

        cant_salir = aux.menu_agregar_producto(todas_categorias)
        categoria = aux.mostrar_listado(todas_categorias + [cant_salir], "Elegi una opcion (numero): ")


#  ELIMINAR PRODUCTO

def eliminar_producto(ids, nombres, categorias, marcas, precios, stocks, stock_minimo):
    print(verde + "\n-- ELIMINAR PRODUCTO --------------------" + blanco)
    mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
    if len(ids) > 0:
        id_str = input("ID del producto a eliminar (salir para cancelar): ").capitalize()
        while id_str != "Salir":
            indice = aux.procesar_y_buscar_id(ids, id_str)
            if indice == -1:
                print(rojo + "  ID no encontrado." + blanco)
            else:
                if stocks[indice] > 0:
                    print(rojo + "  El producto tiene stock. No se puede eliminar." + blanco)
                else:
                    confirmar = input("  Eliminar '" + nombres[indice] + "'? (s/n): ").lower()
                    if confirmar == "s":
                        ids.pop(indice)
                        nombres.pop(indice)
                        categorias.pop(indice)
                        marcas.pop(indice)
                        precios.pop(indice)
                        stocks.pop(indice)
                        stock_minimo.pop(indice)
                        print("  Producto eliminado.")
                    else:
                        print("  Operacion cancelada.")
            mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
            id_str = input("ID del producto a eliminar (salir para cancelar): ").capitalize()


# Modificar Stock (por nombre, segun decision del equipo)

def modificar_stock(ids, nombres, categorias, precios, stocks, stock_minimo):
    print(verde + "\n-- MODIFICAR STOCK ----------------------" + blanco)
    mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
    if len(ids) > 0:
        nombre_str = input("Nombre del producto (salir para cancelar): ")
        if nombre_str == "salir":
            print("  Operacion cancelada.")
        else:
            indice = aux.buscar_indice_por_nombre(nombres, nombre_str)
            if indice == -1:
                print(rojo + "  Producto no encontrado." + blanco)
            else:
                print("  Producto: " + nombres[indice])
                print("  Stock actual: " + str(stocks[indice]))
                print("  1. Sumar stock")
                print("  2. Restar stock")
                print("  3. Establecer stock exacto")
                op = input("  Opcion: ")
                cantidad_str = input("  Cantidad: ")

                if op != "1" and op != "2" and op != "3":
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

def modificar_precio(ids, nombres, categorias, precios, stocks, stock_minimo):
    print(verde + "\n-- MODIFICAR PRECIO ---------------------" + blanco)
    mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
    if len(ids) > 0:
        id_str = input("ID del producto (salir para cancelar): ").capitalize()
        if id_str == "Salir":
            print("  Operacion cancelada.")
        else:
            indice = aux.procesar_y_buscar_id(ids, id_str)
            if indice == -1:
                print(rojo + "  ID no encontrado." + blanco)
            else:
                print("  Producto: " + nombres[indice])
                print("  Precio actual: $" + str(precios[indice]))
                precio_str = input("  Nuevo precio ($): ")
                if not aux.es_numero_decimal(precio_str) or float(precio_str) < 0:
                    print("  Precio invalido.")
                else:
                    precios[indice] = float(precio_str)
                    print("  Precio actualizado a $" + precio_str + ".\n")


#  RF04 — CONFIGURAR STOCK MINIMO

def configurar_stock_minimo(ids, nombres, categorias, precios, stocks, stock_minimo):
    '''Configura el stock minimo de forma masiva (todos) o puntual (por ID).'''
    print(verde + "\n-- CONFIGURAR STOCK MINIMO --------------" + blanco)
    mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
    if len(ids) > 0:
        print("  1. Establecer el mismo minimo para TODOS")
        print("  2. Modificar el minimo de un producto puntual (por ID)")
        op = input("  Opcion: ")
        if op == "1":
            val = input("  Stock minimo para todos: ")
            if not aux.es_numero_entero(val) or int(val) < 0:
                print(rojo + "  Valor invalido." + blanco)
            else:
                k = 0
                while k < len(stock_minimo):
                    stock_minimo[k] = int(val)
                    k = k + 1
                print("  Stock minimo actualizado para todos los productos.\n")
        elif op == "2":
            id_str = input("  ID del producto: ").capitalize()
            indice = aux.procesar_y_buscar_id(ids, id_str)
            if indice == -1:
                print(rojo + "  ID no encontrado." + blanco)
            else:
                val = input("  Nuevo stock minimo: ")
                if not aux.es_numero_entero(val) or int(val) < 0:
                    print(rojo + "  Valor invalido." + blanco)
                else:
                    stock_minimo[indice] = int(val)
                    print("  Stock minimo actualizado.\n")
        else:
            print(rojo + "  Opcion invalida." + blanco)


#  RF08 — GESTION DE CATALOGO (ABM en una opcion)

def gestionar_catalogo(todas_categorias, todas_nombres):
    '''ABM del catalogo en una sola opcion (alta, baja, modificacion). No permite
    nombres repetidos. Comparte la seleccion de categoria/producto para no repetir
    algoritmos.'''
    print(verde + "\n-- GESTION DE CATALOGO (ABM) ------------" + blanco)
    print("  1. Ver Catalogo")
    print("  2. Alta de producto")
    print("  3. Baja de producto")
    print("  4. Modificar producto")
    print("  5. Volver")
    op = input("  Opcion: ")
    if op == "1":
        print("\n--- CATÁLOGO DE PRODUCTOS ---")

        i = 0
        cantidad_categorias = len(todas_categorias)
        while i < cantidad_categorias:
            print(f"\n[{i + 1}] Categoría: {todas_categorias[i]}")

            j = 0
            cantidad_productos = len(todas_nombres[i])
            while j < cantidad_productos:
                print(f"    {i + 1}.{j + 1} - {todas_nombres[i][j]}")
                j += 1

            i += 1
        print("\n─────────────────────────────────────")
        

    if op == "2" or op == "3" or op == "4":
        categoria = aux.mostrar_listado(todas_categorias, "Elegi una categoria (numero): ")
        idx_cat = aux.indice_categoria(categoria, todas_categorias)
        lista_nombres = todas_nombres[idx_cat]

        if op == "2":
            nuevo = input("Nombre del nuevo producto: ")
            if not aux.validar_descripcion(nuevo):
                print(rojo + "  Nombre invalido (vacio o no empieza con letra)." + blanco)
            elif aux.nombre_existe_en_catalogo(todas_nombres, nuevo):
                print(rojo + "  Ese nombre ya existe en el catalogo. No se permiten repetidos." + blanco)
            else:
                lista_nombres.append(nuevo)
                print("  Producto agregado al catalogo en '" + categoria + "'.\n")
        else:
            if len(lista_nombres) == 0:
                print(rojo + "  Esa categoria no tiene productos en el catalogo." + blanco)
            else:
                elegido = aux.mostrar_listado(lista_nombres, "Elegi el producto (numero): ")
                if op == "3":
                    lista_nombres.remove(elegido)
                    print("  Producto '" + elegido + "' eliminado del catalogo.\n")
                else:
                    nuevo = input("Nuevo nombre: ")
                    if not aux.validar_descripcion(nuevo):
                        print(rojo + "  Nombre invalido (vacio o no empieza con letra)." + blanco)
                    elif aux.nombre_existe_en_catalogo(todas_nombres, nuevo):
                        print(rojo + "  Ese nombre ya existe en el catalogo. No se permiten repetidos." + blanco)
                    else:
                        indice = lista_nombres.index(elegido)
                        lista_nombres[indice] = nuevo
                        print("  Producto actualizado a '" + nuevo + "'.\n")


#  BUSCAR PRODUCTO

def buscar_producto(ids, nombres, categorias, marcas, precios, stocks, stock_minimo):
    print("\n-- BUSCAR PRODUCTO ----------------------")
    termino = input("Nombre, categoria o marca: ").lower()
    res_ids = []
    res_nombres = []
    res_categorias = []
    res_precios = []
    res_stocks = []
    res_minimo = []
    i = 0
    while i < len(ids):
        if termino in nombres[i].lower() or termino in categorias[i].lower() or termino in marcas[i].lower():
            res_ids.append(ids[i])
            res_nombres.append(nombres[i])
            res_categorias.append(categorias[i])
            res_precios.append(precios[i])
            res_stocks.append(stocks[i])
            res_minimo.append(stock_minimo[i])
        i = i + 1
    if len(res_ids) == 0:
        print("  No se encontraron productos con '" + termino + "'.\n")
    else:
        mostrar_inventario(res_ids, res_nombres, res_categorias, res_precios, res_stocks, res_minimo)


#  RF06 / RF07 — VENTA

def venta(ids, nombres, categorias, precios, stocks, stock_minimo, vent_total, vent_cant, vent_prod, medios_p):
    '''Registra una venta: resta stock, calcula el total segun medio de pago
    (tarjeta +10% / efectivo con vuelto) y guarda la venta.'''
    aux_nom = []
    aux_cant = []
    total = 0
    print(verde + "\n -- MENU DE VENTAS ---------------------" + blanco)
    mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
    id_str = input("Seleccione el ID del articulo (-1 para terminar): ").capitalize()
    while id_str != "-1":
        indice = aux.procesar_y_buscar_id(ids, id_str)
        if indice == -1:
            print(rojo + "  ID no encontrado." + blanco)
        else:
            print("  Producto: " + nombres[indice])
            print("  Precio actual: $" + str(precios[indice]))
            print("  Cantidad en stock: " + str(stocks[indice]))
            opcion = input("Cuantos desea comprar?: ")
            if not opcion.isdigit() or int(opcion) < 1:
                print(rojo + "Error: cantidad invalida" + blanco)
            elif stocks[indice] < int(opcion):
                print(rojo + "  Error: No hay suficiente stock disponible." + blanco)
            else:
                stocks[indice] = stocks[indice] - int(opcion)
                total = total + float(precios[indice]) * int(opcion)
                print(verde + " !Producto agregado! Total hasta el momento: $" + str(total) + blanco)
                aux_nom.append(nombres[indice])
                aux_cant.append(int(opcion))
        mostrar_inventario(ids, nombres, categorias, precios, stocks, stock_minimo)
        id_str = input("Seleccione el ID del articulo (-1 para terminar la seleccion): ").capitalize()

    if total > 0:
        print(verde + "\nTotal a pagar: $" + str(total) + blanco + "\n")
        print("  Opciones de pago:")
        print("  1. Tarjeta de debito o credito (recargo del 10%)")
        print("  2. Efectivo o transferencia")
        op = input("Seleccione el medio de pago: ")
        while op != "1" and op != "2":
            print(rojo + "Opcion invalida, intente de nuevo" + blanco)
            op = input("Seleccione el medio de pago: ")
        medio = ""
        if op == "1":
            total = total * 1.10
            medio = "Tarjeta"
            print(verde + "\n  Se aplico un 10% de recargo por tarjeta." + blanco)
        else:
            medio = "Efectivo/transf"
            # RF07: pedir importe entregado y calcular el vuelto
            pago_str = input("  Importe entregado ($): ")
            while not aux.es_numero_decimal(pago_str) or float(pago_str) < total:
                print(rojo + "  Importe insuficiente o invalido." + blanco)
                pago_str = input("  Importe entregado ($): ")
            vuelto = float(pago_str) - total
            print("  Vuelto total: $" + ("%.2f" % vuelto))
            aux.calcular_vuelto(vuelto)
        print(verde + "\n" + "=" * 50 + blanco)
        print("  Total final a pagar: $" + ("%.2f" % total))
        print(verde + "=" * 50 + blanco)
        vent_total.append(float(total))
        vent_cant.append(aux_cant)
        vent_prod.append(aux_nom)
        medios_p.append(medio)
        print(" [SISTEMA] Venta y desglose de articulos guardados.")


def inf_vent(vent_cant, vent_total, vent_prod, medios_p):
    '''Muestra un informe de las ventas del dia (cantidad, productos, medio de
    pago y total) y la recaudacion total.'''
    print(verde + "\n" + "=" * 50)
    print("  REPORTE DETALLADO DE VENTAS DEL DIA")
    print("=" * 50 + blanco)
    if len(vent_total) == 0:
        print("  No se registraron ventas hoy.")
    else:
        recaudacion_total = 0
        i = 0
        while i < len(vent_total):
            print("\n  * VENTA #" + str(i + 1) + " *")
            print("  Medio de Pago: " + medios_p[i])
            print("  Detalle de Articulos:")
            j = 0
            while j < len(vent_prod[i]):
                print("    - " + str(vent_cant[i][j]) + " un. x " + vent_prod[i][j])
                j = j + 1
            print("  Total Facturado: $" + ("%.2f" % vent_total[i]))
            print("-" * 35)
            recaudacion_total = recaudacion_total + vent_total[i]
            i = i + 1
        print(verde + "\n" + "=" * 50)
        print("  RECAUDACION TOTAL DE LA CAJA: " + blanco + "$" + ("%.2f" % recaudacion_total))
        print(verde + "=" * 50 + blanco + "\n")


# MAIN DE PRUEBA DEL MODULO (RT05)
def prueba():
    print("== Prueba de funcion_final ==")
    todas_categorias, todas_nombres, marcas_disponibles = crear_catalogo()
    ids = ["Tec752", "Mon540", "Mou123"]
    nombres = ["Logitech Teclado membrana compacto", "Corsair Monitor 24 Full HD", "Razer Mouse gaming 16000 DPI"]
    categorias = ["Teclado", "Monitor", "Mouse"]
    marcas = ["Logitech", "Corsair", "Razer"]
    precios = [100.0, 200.0, 300.0]
    stocks = [10, 20, 3]
    stock_minimo = [5, 5, 5]
    informe_general(ids, nombres, categorias, marcas, precios, stocks, stock_minimo)


if __name__ == "__main__":
    prueba()
