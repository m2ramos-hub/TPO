#Pro-Gamer Logistics
import auxiliar_f2 as aux
import funcion_f2 as fn

# Colores
rojo = "\033[31m"
blanco = "\033[0m"


def main():
    todas_categorias, todas_nombres, marcas_disponibles = fn.crear_catalogo()

    # Inventario: 7 listas paralelas, alineadas por indice. (RT06: 3 precargados)
    ids          = ["Tec752", "Mon540", "Mou123"]
    nombres      = ["Logitech Teclado membrana compacto", "Corsair Monitor 24 Full HD", "Razer Mouse gaming 16000 DPI"]
    categorias   = ["Teclado", "Monitor", "Mouse"]
    marcas       = ["Logitech", "Corsair", "Razer"]
    precios      = [100.0, 200.0, 300.0]
    stocks       = [10, 20, 30]
    stock_minimo = [5, 5, 5]

    # Registro de ventas (RT07: creadas aca, no como variables globales)
    vent_total = []
    vent_cant  = []
    vent_prod  = []
    medios_p   = []

    print("\n  Bienvenido al sistema de inventario de Pro-Gamer Logistics.\n")

    aux.mostrar_menu()
    opcion = input("  Opcion: ")

    while opcion != "6":
        if opcion == "1":
            aux.menu_gestion()
            sub = input("  Seleccione: ")
            while sub != "4":
                if sub == "1":
                    fn.agregar_producto(ids, nombres, categorias, marcas, precios, stocks, stock_minimo, todas_categorias, todas_nombres, marcas_disponibles)
                elif sub == "2":
                    fn.eliminar_producto(ids, nombres, categorias, marcas, precios, stocks, stock_minimo)
                elif sub == "3":
                    aux.menu_modificar()
                    sub2 = input("  Seleccione: ")
                    while sub2 != "3":
                        if sub2 == "1":
                            fn.modificar_stock(ids, nombres, categorias, precios, stocks, stock_minimo)
                        elif sub2 == "2":
                            fn.modificar_precio(ids, nombres, categorias, precios, stocks, stock_minimo)
                        else:
                            print(f"{rojo}  Opcion invalida. Intenta de nuevo.{blanco}")
                        aux.menu_modificar()
                        sub2 = input("  Seleccione: ")
                else:
                    print(f"{rojo}  Opcion invalida. Intenta de nuevo.{blanco}")
                aux.menu_gestion()
                sub = input("  Seleccione: ")
        elif opcion == "2":
            fn.venta(ids, nombres, categorias, precios, stocks, stock_minimo, vent_total, vent_cant, vent_prod, medios_p)
        elif opcion == "3":
            fn.informe_general(ids, nombres, categorias, marcas, precios, stocks, stock_minimo)
        elif opcion == "4":
            fn.configurar_stock_minimo(ids, nombres, categorias, precios, stocks, stock_minimo)
        elif opcion == "5":
            fn.gestionar_catalogo(todas_categorias, todas_nombres)
        else:
            print(f"{rojo}  Opcion invalida. Intenta de nuevo.{blanco}")
        aux.mostrar_menu()
        opcion = input("  Opcion: ")
    print("\n  Saliendo del sistema. Hasta luego!\n")


if __name__ == "__main__":
    main()
