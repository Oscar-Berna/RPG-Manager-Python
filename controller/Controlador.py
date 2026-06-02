from model.Personaje import Guerrero, Mago, Arquero
from db.conexion import (crear_personaje, listar_personajes,
                          buscar_por_nombre, actualizar_nivel,
                          eliminar_personaje)
from view.Menu import (mostrar_personajes, mostrar_personaje,
                        pedir_datos_personaje)

def crear_nuevo():
    nombre, clase = pedir_datos_personaje()
    if   clase in ('1', 'Guerrero', 'guerrero'): p = Guerrero(nombre)
    elif clase in ('2', 'Mago',     'mago'):     p = Mago(nombre)
    elif clase in ('3', 'Arquero',  'arquero'):  p = Arquero(nombre)
    else:
        print('Clase invalida.')
        return
    try:
        crear_personaje(p)
    except Exception as e:
        print(f'Error al crear: {e}')

def listar():
    try:
        mostrar_personajes(listar_personajes())
    except Exception as e:
        print(f'Error al listar: {e}')

def buscar():
    nombre = input('Nombre a buscar: ').strip()
    try:
        mostrar_personaje(buscar_por_nombre(nombre))
    except Exception as e:
        print(f'Error al buscar: {e}')

def actualizar():
    try:
        id    = int(input('ID del personaje: '))
        nivel = int(input('Nuevo nivel (1-50): '))
        actualizar_nivel(id, nivel)
    except ValueError:
        print('Error: ingresa numeros validos.')
    except Exception as e:
        print(f'Error: {e}')

def eliminar():
    try:
        id = int(input('ID a eliminar: '))
        eliminar_personaje(id)
    except ValueError:
        print('Error: ingresa un numero valido.')
    except Exception as e:
        print(f'Error: {e}')

def habilidad():
    try:
        personajes = listar_personajes()
        mostrar_personajes(personajes)
        id = int(input('ID del personaje: '))
        p  = next((x for x in personajes if x.id == id), None)
        if p:
            if   p.clase == 'Guerrero': obj = Guerrero(p.nombre, p.nivel)
            elif p.clase == 'Mago':     obj = Mago(p.nombre, p.nivel)
            elif p.clase == 'Arquero':  obj = Arquero(p.nombre, p.nivel)
            print(obj.habilidad_especial())
        else:
            print('ID no encontrado.')
    except Exception as e:
        print(f'Error: {e}')
