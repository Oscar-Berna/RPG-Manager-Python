import mysql.connector # type: ignore

def get_connection():
    return mysql.connector.connect(
        host     = '127.0.0.1',
        user     = 'root',
        password = '',
        database = 'rpg_manager'
    )

def crear_personaje(p):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('''INSERT INTO personaje
                   (nombre, clase, nivel, vida, vida_maxima, ataque, defensa)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                (p.nombre, p.clase, p.nivel, p.vida,
                 p.vida_maxima, p.ataque, p.defensa))
    conn.commit()
    cur.close()
    conn.close()
    print(f'Personaje {p.nombre} creado correctamente.')

def listar_personajes():
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('SELECT * FROM personaje')
    filas = cur.fetchall()
    cur.close()
    conn.close()
    from model.Personaje import Personaje
    return [Personaje(f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[0]) for f in filas]

def buscar_por_nombre(nombre):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('SELECT * FROM personaje WHERE nombre = %s', (nombre,))
    f = cur.fetchone()
    cur.close()
    conn.close()
    if f:
        from model.Personaje import Personaje
        return Personaje(f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[0])
    return None

def actualizar_nivel(id, nuevo_nivel):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('UPDATE personaje SET nivel = %s WHERE id = %s', (nuevo_nivel, id))
    if cur.rowcount == 0:
        print(f'Error: ID {id} no encontrado.')
    else:
        conn.commit()
        print(f'Nivel actualizado a {nuevo_nivel}.')
    cur.close()
    conn.close()

def eliminar_personaje(id):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute('DELETE FROM personaje WHERE id = %s', (id,))
    if cur.rowcount == 0:
        print(f'Error: ID {id} no encontrado.')
    else:
        conn.commit()
        print(f'Personaje con ID {id} eliminado.')
    cur.close()
    conn.close()
