#coding=utf-8
"""
Módulo para la gestión de los métodos que se encargan de la facturación.

"""
import funcioneservicios,variables
def calcprezo(prezo, noches):
    """
    Función que calcula lo que tiene que pagar un cliente por determinadas noches
    Multiplica el precio de la habitación por el número de noches

    :param prezo: contiene el precio de la habitacion.
    :param noches: contiene el numero de noches que va a pasar el cliente el la habitación.
    :return: devuelve el total que tiene que pagar el cliente

    """
    try:
        resul = prezo * noches
        return resul
    except Exception as e:
        print('Error calcular precio', e)

def cargardatos(total):
    """
    En la parte de la facutura carga todos los servicios que tiene una reserva determinada.
    Carga el concepto y el precio de cada servicio.

    :param total: Contiene el total de la factura.
    :return: No devuelve nada.

    """
    lista = funcioneservicios.serviciosreser(str(variables.codr))
    if lista != None:
        con = 0
        i = 0
        while con != len(lista):
            i = i + 1
            variables.lblfacturas[5][i].set_text(str(lista[con][0]))
            variables.lblfacturas[8][i].set_text(str(lista[con][1]))
            total = total + lista[con][1]
            con = con + 1

        calculaprecio(total)

    return total


def calculaprecio(subtotal):
    subtotal = round(subtotal,2)
    variables.lblfacturas[10].set_text(str(subtotal)+' €')
    iva = subtotal *0.21
    iva = round(iva, 2)
    variables.lblfacturas[11].set_text(str(iva)+' €')
    total = subtotal + iva
    variables.lblfacturas[9].set_text(str(total)+' €')


def borrardatos():
    """
    Método que se encarga de borrar todos los label de servicios de la parte de la facturación.
    Recorre todos los label de facturación y los vacia.

    :return: No devuelve nada.

    """
    try:
        lista = funcioneservicios.serviciosreser(str(variables.codr))
        if lista != None:
            con = 0
            i = 0
            while con != len(lista):
                i = i + 1
                variables.lblfacturas[5][i].set_text("")
                variables.lblfacturas[8][i].set_text("")
                con = con + 1
    except:
        print('Error borrar datos')

def limpiardatosclifactura():
    """
    Método que se encarga de borra los label de los datos del cliente en la parte de facturación
    Recorre todos los label y los vacia.

    :return: No devuelve nada.

    """
    try:
        for i in range(5):
            variables.lblfacturas[i].set_text('')
        variables.lblfacturas[9].set_text('')
        variables.lblfacturas[10].set_text('')
        variables.lblfacturas[11].set_text('')


    except:
        print('Error limpiar datos factura')

def limpiarfactura():
    """
    Método que se encarga de borrar los label de servicios de la parte de facutracion

    :return: No devuelve nada.

    """
    for i in range(len(variables.conceptofac)):
        variables.conceptofac[i].set_text('')
        variables.unidadfac[i].set_text('')
        variables.preciofac[i].set_text('')
        variables.totalfac[i].set_text('')
