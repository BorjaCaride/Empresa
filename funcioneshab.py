#coding=utf-8
"""
Módulo que gestiona las habitaciones.

Aquí vendrán todas las funciones que afectan a la ¡gestión de las
habitaciones.

"""

import conexion, sqlite3, variables

def insertarhab(fila):
    """
    Inserta en la base de datos una nueva habitacion.
    :param fila: Contiene los datos de la habitacion.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('insert into habitacion(numero,tipo,prezo,libre) values(?,?,?,?)', fila)
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listarhab():
    """
    Lista todos los datos de todas las habitaciones.
    :return: Devuelve una lista con los datos de las habitaciones.

    """
    try:
        conexion.cur.execute('select * from habitacion')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def limpiarentry(fila):
    """
    Vaciará el contenido de los entry.
    :param fila: Contiene el contenido de los entry.
    :return: No devuelve nada.

    """
    for i in range(len(fila)):
        fila[i].set_text('')

def listadohab(listhab):
    """
    Lista todas los datos de las habitaciones y lo añade al treeview.
    :param listhab: Contiene la lista que se va a ver en el treeview.
    :return: No devuelve nada.

    """
    try:
        variables.listado = listarhab()
        variables.listhab.clear()
        for registro in variables.listado:
            listhab.append(registro)
    except:
        print("error en cargar treeview de hab")


def bajahab(numhab):
    """
    Da de baja un cliente en la base de datos.
    :param numhab: Contiene el número de habitación.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('delete from habitacion where numero = ?', (numhab,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def modifhab(registro, numhab):
    """
    Modifica en la base de datos una habitación.
    :param registro: Contiene los nuevos datos de la habitación.
    :param numhab: Contiene el número de la habitación.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('update habitacion set tipo = ?, prezo = ?, libre = ? where numero = ?',
                             (registro[1], registro[0], registro[2], numhab))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadonumhab(self):
    """
    Obtiene el número de habitación de todas las habitaciones y lo añade a la combobox.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('select numero from habitacion')
        listado = conexion.cur.fetchall()
        variables.listcmbhab.clear()
        for row in listado:
            variables.listcmbhab.append(row)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadonumhabres():
    """
    Obtiene el número de todas las habitaciones.
    :return: Devuelve una lista con todos los números.

    """
    try:
        conexion.cur.execute('select numero from habitacion')
        lista = conexion.cur.fetchall()
        return lista
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def cambiaestadohab(libre, numhabres,op):
    """
    Función que cambia el estado de una habitación.
    :param libre: Contiene si la habitación esta libre o no.
    :param numhabres: Contiene el numero de la habitación de la reserva.
    :param op:
    :return: No devuelve nada.
    """
    try:
        if op ==0:
            estado = libre[0]
        else :
            estado = libre
        conexion.cur.execute('update habitacion set libre = ? where numero = ?',
                             (estado, numhabres))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
       print(e)
       conexion.conex.rollback()