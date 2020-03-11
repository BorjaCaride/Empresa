#coding=utf-8
import os, threading, sys
import sqlite3
from datetime import datetime, date
import time
import conexion, zipfile
import variables

def backup():
    """
    Método que realiza una copia de seguridad.
    Se encarga de coger empresa.sqlite y añadirlo a un archivo .zip con la fecha y el nombre
    :return:
    """
    try:
        conexion.Conexion().cerrarbbdd()
        backup = 'backup.zip'
        copia = zipfile.ZipFile(backup, 'w')
        copia.write('empresa.sqlite', compress_type = zipfile.ZIP_DEFLATED)
        copia.close()
        neobackup = str(datetime.now()) + str(backup)
        os.rename(backup, neobackup)
        conexion.Conexion().abrirbbdd()
        return neobackup
    except:
        print('error backup')

def controlhab():
    """
    Método que comprueba que la fecha mínima que ha insertado el usuario tiene que ser como mínimo la de hoy.

    :return: No devuelve nada.
    """
    variables.t = threading.Timer(0.5, controlhab)
    variables.t.daemon = True
    variables.t.start()
    fechahoy = time.strftime('%H:%M:%S')
    fechacontrol = '20:08:00'
    if str(fechacontrol) == str(fechahoy):
        actualizarhab()

def cerrartimer():
    variables.t.join(0)



def actualizarhab():
    print('hola actualizasdor de habitaciones')

def preciosbasicos():
    try:
        conexion.cur.execute('select * from prezos')
        listadoprezos = conexion.cur.fetchone()
        conexion.conex.commit()
        return listadoprezos

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()