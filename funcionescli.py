#coding=utf-8
""" Módulo que gestiona los clientes.

"""

import conexion
import sqlite3
import variables

def limpiarentry(fila):
    """
    Método que se encarga de limpiar los entry de la ventana de clientes
    Se encarga de recorrer todos los entry y vaciarlos.
    :param fila: contiene los datos.
    :return: no devuelve nada.

    """
    try:
        variables.menslabel[1].set_text('')
        for i in range(len(fila)):
            fila[i].set_text('')
    except:
        print('Error al limpiar datos')

def validoDNI(dni):
    """
    Método para validar un dni.
    Se encarga de verificar si el dni introducido por el usuario es válido, comprobando su longitud(9) y que al final tenga letra.

    :param dni: contiene el dni del usuario.
    :return: si el dni es valido True, si el dni no es valido False.

    """
    try:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = dni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                print(dni)
                dni = dni.replace(dni[0],reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control
        return False
    except:
        print("Error")
        return None


def insertarcli(fila):
    """
    Método que se encarga de insertar un cliente nuevo en la base de datos

    :param fila: contiene los datos del cliente.
    :return: no devuelve nada.

    """
    try:
        conexion.cur.execute('insert into  clientes(dni,apel,nome, data) values(?,?,?,?)',fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listar():
    """
    Metodo que lista a todos los clientes que se encuentran en la base de datos.

    :return: devuelve una lista con todos los clientes.

    """
    try:
        conexion.cur.execute('select * from clientes')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajacli(dni):
    """
    Método que se encarga de dar de baja un cliente.-
    Con el dni que se le pasa busca el cliente en la base de datos y lo borra.

    :param dni: contiene el dni del cliente.
    :return: no devuelve nada.

    """
    try:
        conexion.cur.execute('delete from clientes where dni = ?', (dni,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def modifcli(registro, cod):
    """
    Este método se encarga de modificar un determinado cliente.
    Se busca el cliente por el id en la base de datos y se vuelven a guardar todos los campos.

    :param registro: contiene los datos del cliente.
    :param cod: contiene el codigo del cliente.
    :return: no devuelve nada.

    """
    try:
        conexion.cur.execute('update clientes set dni = ?, apel= ?, nome = ?, data = ? where id = ?',
                             (registro[0], registro[1], registro[2], registro[3], cod))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadocli(listclientes):
    """
    Método que lista todos los clientes de la base de datos y los añade al treeview de la ventana de clientes.

    :param listclientes: contiene la lista de clientes.
    :return: añade en el tree los clientes que hay en la bd.

    """
    try:
        variables.listado = listar()
        listclientes.clear()
        for registro in variables.listado:
            listclientes.append(registro[1:5])
    except:
        print("error en cargar treeview")


def selectcli(dni):
    """
    Método que busca en la base de datos un cliente por el dni y recoge el id.

    :param dni: contiene el dni del cliente.
    :return: devuelve los datos del cliente.

    """
    try:
        conexion.cur.execute('select id from clientes where dni = ?', (dni,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()
