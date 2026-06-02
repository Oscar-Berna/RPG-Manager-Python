from controller.Controlador import (crear_nuevo, listar, buscar,
                                     actualizar, eliminar, habilidad)
from view.Menu import mostrar_menu, pedir_opcion

while True:
    mostrar_menu()
    opcion = pedir_opcion()

    if   opcion == '1': crear_nuevo()
    elif opcion == '2': listar()
    elif opcion == '3': buscar()
    elif opcion == '4': actualizar()
    elif opcion == '5': eliminar()
    elif opcion == '6': habilidad()
    elif opcion == '0':
        print('Hasta luego!')
        break
    else:
        print('Opcion invalida.')
