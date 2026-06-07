import funciones as fn


def main():
    inventario = []
    print("\n  Bienvenido al sistema de inventario de Pro-Gamer Logistics.\n")

    fn.mostrar_menu()
    opcion = int(input("  Opcion: "))

    while opcion != 8:
        if opcion == 1:
            fn.agregar_producto(inventario)
        elif opcion == 2:
            fn.eliminar_producto(inventario)
        elif opcion == 3:
            print("  1. Modificar stock")
            print("  2. Modificar precio")
            sub = int(input("  Seleccione: "))
            if sub == 1:
                fn.modificar_stock(inventario)
            elif sub == 2:
                fn.modificar_precio(inventario)
            else:
                print("  Opcion invalida.")
        elif opcion == 4:
            fn.informe_general(inventario)
        else:
            print("\n  Opcion invalida. Intentá de nuevo.\n")

        fn.mostrar_menu()
        opcion = int(input("  Opcion: "))
    print("\n  Saliendo del sistema. Hasta luego!\n")


if __name__ == "__main__":
    main()
