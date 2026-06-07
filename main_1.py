import funciones_1 as fn


def main():
    # El inventario ahora son 6 listas paralelas, alineadas por indice.
    ids        = []
    nombres    = []
    categorias = []
    marcas     = []
    precios    = []
    stocks     = []
    print("\n  Bienvenido al sistema de inventario de Pro-Gamer Logistics.\n")

    fn.mostrar_menu()
    opcion = int(input("  Opcion: "))

    while opcion != 8:
        if opcion == 1:
            fn.agregar_producto(ids, nombres, categorias, marcas, precios, stocks)
        elif opcion == 2:
            fn.eliminar_producto(ids, nombres, categorias, marcas, precios, stocks)
        elif opcion == 3:
            print("  1. Modificar stock")
            print("  2. Modificar precio")
            sub = int(input("  Seleccione: "))
            if sub == 1:
                fn.modificar_stock(ids, nombres, categorias, precios, stocks)
            elif sub == 2:
                fn.modificar_precio(ids, nombres, categorias, precios, stocks)
            else:
                print("  Opcion invalida.")
        elif opcion == 4:
            fn.informe_general(ids, nombres, categorias, marcas, precios, stocks)
        else:
            print("\n  Opcion invalida. Intentá de nuevo.\n")
        fn.mostrar_menu()
        opcion = int(input("  Opcion: "))
    print("\n  Saliendo del sistema. Hasta luego!\n")
if __name__ == "__main__":
    main()