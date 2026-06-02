def mostrar_menu():
    print('\n========== RPG MANAGER ==========')
    print('1. Crear personaje')
    print('2. Listar personajes')
    print('3. Buscar personaje por nombre')
    print('4. Actualizar nivel')
    print('5. Eliminar personaje')
    print('6. Ver habilidad especial')
    print('0. Salir')
    print('==================================')

def mostrar_personajes(personajes):
    if not personajes:
        print('No hay personajes registrados.')
        return
    print('\n--- PERSONAJES ---')
    for p in personajes:
        print(f'ID:{p.id} | {p}')

def mostrar_personaje(p):
    if p:
        print(f'\nEncontrado: {p}')
    else:
        print('Personaje no encontrado.')

def pedir_opcion():
    return input('\nElige una opcion: ').strip()

def pedir_datos_personaje():
    nombre = input('Nombre: ').strip()
    print('Clases: 1-Guerrero  2-Mago  3-Arquero')
    clase  = input('Clase (numero o nombre): ').strip()
    return nombre, clase
