#coding=utf-8
"""
Módulo que gestiona las reservas.

"""
import conexion
import sqlite3
import variables
from datetime import datetime

def limpiarentry(fila):
    """
    Limpia los entrys de las reservas.
    :param fila: Contiene los entrys.
    :return: No devuelve nada.

    """

    for i in range(len(fila)):
        fila[i].set_text('')
    for i in range(len(variables.menslabel)):
        variables.menslabel[i].set_text('')
    variables.cmbhab.set_active(-1)

def calculardias():
    """
    Valida que la fecha de salida sea posterior a la de entrada y calcula el número de noches.
    :return: No devuelve nada.

    """
    diain = variables.filareserva[2].get_text()
    date_in = datetime.strptime(diain, '%d/%m/%Y').date()
    diaout = variables.filareserva[3].get_text()
    date_out = datetime.strptime(diaout, '%d/%m/%Y').date()
    noches = (date_out-date_in).days
    if noches <= 0:
        variables.menslabel[2].set_text('Check-Out debe ser posterior')
        variables.reserva = 0
    else:
        variables.reserva = 1
        variables.menslabel[2].set_text(str(noches))

def insertares(fila):
    """
    Inserta una reserva en la base de datos.
    :param fila: Contiene los datos de la reserva.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('insert into  reservas(dni, numhab, checkin, checkout, noches) values(?,?,?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadores():
    """
    Lista todas las reservas y las muestra en el treeview
    :return: No devuelve nada.

    """
    try:
        variables.listado = listares()
        variables.listreservas.clear()
        for registro in variables.listado:
            variables.listreservas.append(registro)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listares():
    """
    Lista las reservas
    :return: Devuelve una lista con todas las reservas.

    """
    try:
        conexion.cur.execute('select codreser, dni, numhab, checkin, checkout, noches from reservas')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarapelcli(dni):
    """
    Busca en la base de datos el apellido de un determinado cliente.
    :param dni: Contiene el dni del cliente.
    :return: Devuelve el apellido del cliente.

    """
    try:
        conexion.cur.execute('select apel from clientes where dni = ?', (dni,))
        apel = conexion.cur.fetchone()
        conexion.conex.commit()
        return apel
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarnomecli(dni):
    """
    Busca en la base de datos el nombre de un determinado cliente.
    :param dni: Contiene el dni del cliente.
    :return: Devuelve el nombre del cliente.

    """
    try:
        conexion.cur.execute('select nome from clientes where dni = ?', (dni,))
        nombre = conexion.cur.fetchone()
        conexion.conex.commit()
        return nombre
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarpreciohab(numhab):
    """
    Busca en la base de datos el precio de una determinada habitación.
    :param numhab: Contiene el número de la habitación.
    :return: Devuelve el precio de la habitación.

    """
    try:
        conexion.cur.execute('select prezo from habitacion where numero = ?', (numhab,))
        precio = conexion.cur.fetchone()
        conexion.conex.commit()
        return precio
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajareserva(cod):
    """
    Da de baja una reserva en la base de datos y pone el switch de la habitación a libre.
    :param cod: Contiene el codigo de reserva.
    :return: No devuelve nada.

    """
    try:
        conexion.cur.execute('delete from reservas where codreser = ?', (cod,))
        conexion.conex.commit()
        if variables.switch.get_active():
            libre = 'SI'
        else:
            libre = 'NO'
    except sqlite3.OperationalError as e:
        print('Error baja reserva')
        conexion.conex.rollback()

def versilibre(numhab):
    """
    Comprueba si una determinada habitación esta libre o no.
    :param numhab: Contiene el número de habitación.
    :return: Devuelve True si esta libre, False si esta ocupada.

    """
    try:
        conexion.cur.execute('select libre from habitacion where numero = ?', (numhab,))
        lista= conexion.cur.fetchone()
        conexion.conex.commit()
        if lista[0] == 'SI':
            return True
        else:
            return False
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()
