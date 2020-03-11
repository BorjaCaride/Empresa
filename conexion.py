#coding=utf-8
"""
Módulo para gestionar los métodos que se encargan de la base de datos.

"""
import os, sqlite3

class Conexion:
    def abrirbbdd(self):
        """
        Metodo para abrir la base de datos
        Se encarga de crear una conexión con empresa.sqlite y notifica que se abrio correctamente.
        :return: No devuelve nada.

        """
        try:
            global bbdd, conex, cur
            bbdd = 'empresa.sqlite'
            conex = sqlite3.connect(bbdd)
            cur = conex.cursor()
            print("Conexión realizada correctamente")
        except sqlite3.OperationalError as e:
            print("Error al abrir: ", e)

    def cerrarbbdd(self):
        """
        Método para cerrar la base de datos.
        Se encarga de cerrar correctamente la base de datos y notificar de que se ha cerrado.
        :return: No devuelve nada.

        """
        try:
            cur.close()
            conex.close()
            print("Base de datos cerrada correctamente ")
        except sqlite3.OperationalError as e:
            print("Error al cerrar: ", e)




