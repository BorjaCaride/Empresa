#coding=utf-8
"""
Modulo para la gestion de servicios

"""

import conexion,variables,sqlite3

def insertarserv(fila):
    """
    Inserta un servicio en la base de datos
    :param fila: contiene los datos del servicio(codreserva,concepto y precio)
    :return:no devuelve nada
    """
    try:
        conexion.cur.execute('insert into  servicios(codreserva,concepto,precio) values(?,?,?)',fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listarserv(cod):
    """
    Obtiene
    :param cod: contiene el codigo de reserva
    :return: Devuelve un listado con los datos obtenidos

    """
    try:

        conexion.cur.execute('select codserv,concepto,precio from servicios where codreserva = ?',(cod,))
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadoserv(cod):
    """
    Obtiene todos los datos de los servicios para cargarlo en el treeview.
    :param cod: Contiene el codigo de reserva.
    :return: No devuelve nada.

    """
    try:
        variables.listado = listarserv(cod)
        variables.listserv.clear()
        for registro in variables.listado:
            variables.listserv.append(registro)
    except:
        print("error en cargar treeview de servicios")
def limpiarentry(fila):
    """
    Limpia los entry.
    :param fila: contiene los entry.
    :return: No devuelve nada.

    """
    for i in range(len(fila)):
        fila[i].set_text('')


def serviciosreser(cod):
    """
    Obtiene el concepto y el precio de una determinada reserva.
    :param cod: Contiene el código de reserva.
    :return: Devuelve un listado con los datos obtenidos.

    """
    try:
        conexion.cur.execute('select  concepto,precio from servicios where codreserva = ?',(cod,))
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def comprobar(cod):
    """
    Obtiene el numero de servicios que tiene una reserva.
    :param cod: Contiene el número de reserva.
    :return: Devuelve el numero de servicios.

    """
    try:
        conexion.cur.execute('select  count(concepto) from servicios where codreserva = ?', (cod,))
        listado = conexion.cur.fetchall()
        return listado

        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()
def bajaservicio(cod):
    """
    Se encarga de dar de baja un servicio en la base de datos.
    :param cod: Contiene el codigo de servicio.
    :return: No devuelve nada.

    """

    try:
        conexion.cur.execute('delete from servicios where codserv = ?', (cod,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajaserviciobasico(codresr,nomservicio):
    try:
        conexion.cur.execute('delete from servicios where codserv = ? ', (codresr,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def verprecio(nom):
    """
    Obtiene el precio de un determinado servicio.
    :param nom: Contiene el concepto del servicio.
    :return: Devuelve el precio del concepto.

    """
    try:
        conexion.cur.execute('select precio from precios where concepto = ?',(nom,))
        lista = conexion.cur.fetchall()
        return lista
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()
def servicioSA(cod):
    """
    Borra todos los servicios de una reserva para ponerla en solo alojamiento.
    :param cod: Contiene el codigo de reserva.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('delete from servicios where codreserva = ?',(cod,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def comprobarservicio(cod):
    """
    Obtiene el nombre de los servicios de una determinada reserva
    :param cod: Contiene el código de reserva.
    :return: Devuelve un listado con los nombres de los servicios.

    """
    try:
        conexion.cur.execute('select concepto from servicios where codreserva = ?',(cod,))
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()