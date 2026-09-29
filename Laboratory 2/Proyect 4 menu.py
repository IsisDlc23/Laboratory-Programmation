print("Menú de Comidas")

opcion = -1

while opcion != 0:
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Hot Dog")
    print("4. Papas Fritas")
    print("5. Nachos")
    print("6. Salchipapas")
    print("7. Dorilocos")
    print("0. Salir")

    opcion = int(input("Escoge un menú: "))

    match opcion:
        case 1:
            print("Has pedido una Hamburguesa.")
        case 2:
            print("Has pedido una Pizza.")
        case 3:
            print("Has pedido un Hot Dog.")
        case 4:
            print("Has pedido unas Papas Fritas.")
        case 5:
            print("Has pedido unos Nachos.")
        case 6:
            print("Has pedido unas Salchipapas.")
        case 7:
            print("Has pedido Dorilocos.")
        case 0:
            print("Salir del menú.")
        case _:
            print("Opción inválida. Ese menú no existe, seleccione otra opción.")
            