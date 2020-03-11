#coding=utf-8
"""
Módulo que gestiona la estructura que va a tener la factura en pdf

"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os,conexion,funcioneservicios,variables

import funcionescli


def basico():
    """
    Se encarga de organizar la cabecera de la factura.
    :return:No devuelve nada.

    """
    try:
        text1 = 'Bienvenido a nuestro hotel'
        bill.drawImage('./img/logohotel.png', 475, 680, width=64, height=64)
        bill.setFont('Helvetica-Bold', size=16)
        bill.drawString(250,780,'HOTEL LITE')
        bill.setFont('Times-Italic',size=10)
        bill.drawString(242,765, text1)
        bill.line(50,670,540,670)
        textpie = 'Hotel lite, CIF = 0000000000000A, Tifo = 986000000000 e-mail = info@hotelite.com'
        bill.setFont('Times-Italic',size=8)
        bill.drawString(250,20,textpie)
        bill.line(50, 30, 540, 30)
    except:
        print('ERROR EN BASICO')


def factura(datosfactura):
    """
    Se encarga de organizar las partes de la factura.
    :param datosfactura: Contiene los datos de la factura.
    :return: No devuelve nada.

    """
    try:

        global bill
        bill = canvas.Canvas('factura.pdf', pagesize=A4)
        basico()
        cabecera(datosfactura)
        cuerpo(datosfactura)
        bill.showPage()
        bill.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/factura.pdf')
    except:
        print('Error en módulo factura')

def cabecera(datosfactura):
    """
    Se encarga de organizar la cabecera de la factura.
    :param datosfactura: contiene los datos de la factura.
    :return: No devuelve nada.

    """

    bill.setFont('Helvetica-Bold', size=8)
    text3 = 'Numero de factura:'
    bill.drawString(50, 735, text3)

    bill.setFont('Helvetica', size=8)
    bill.drawString(140, 735, datosfactura[6])

    bill.setFont('Helvetica-Bold', size=8)
    text4 = 'Fecha Factura:'
    bill.drawString(320, 735, text4)

    bill.setFont('Helvetica', size=8)
    bill.drawString(400, 735, datosfactura[5])

    bill.setFont('Helvetica-Bold', size=8)
    text5 = 'DNI CLIENTE:'
    bill.drawString(50, 710, text5)

    bill.setFont('Helvetica', size=8)
    bill.drawString(120, 710, datosfactura[0])

    bill.setFont('Helvetica-Bold', size=8)
    text6 = 'Nº de Habitación:'
    bill.drawString(320, 710, text6)

    bill.setFont('Helvetica', size=8)
    bill.drawString(400, 710, datosfactura[3])

    bill.setFont('Helvetica-Bold', size=8)
    text7 = 'Apellidos:'
    bill.drawString(50, 685, text7)

    bill.setFont('Helvetica', size=8)
    bill.drawString(120, 685, datosfactura[1])

    bill.setFont('Helvetica-Bold', size=8)
    text8 = 'Nombre:'
    bill.drawString(320, 685, text8)

    bill.setFont('Helvetica', size=8)
    bill.drawString(400, 685, datosfactura[2])

def cuerpo(datosfactura):
    """
    Se encarga de organizar el cuerpo de la factura.
    :return: No devuelve nada.

    """
    bill.setFont('Helvetica-Bold', size=10)
    text = ['CONCEPTO','UNIDADES','PRECIO/UNIDAD','TOTAL']
    x = 75
    for i in range(0,4):
        bill.drawString(x,649,text[i])
        x+=130
    bill.line(50,635,540,635)

    y = 615
    x=80


    bill.setFont('Helvetica', size=8)

    bill.drawString(x,y,'Noches')
    x=x+130
    bill.drawString(x,y,str(variables.lblfacturas[6][0].get_text()))
    x=x+130
    bill.drawString(x,y,str(variables.lblfacturas[7][0].get_text()))
    x=x+130
    bill.drawString(x,y,str(variables.lblfacturas[8][0].get_text()))
    x= 80
    y =y-20
    lista = funcioneservicios.serviciosreser(datosfactura[6])
    con =0

    while con != len(lista):

        bill.drawString(x,y,str(lista[con][0]))
        x=x+390
        bill.drawString(x, y, str(lista[con][1]))
        x=80
        y=y-20
        con=con+1

    bill.line(50, 100, 540, 100)

    bill.setFont('Helvetica-Bold', size=8)
    bill.drawString(462,75,'IVA:')
    bill.drawString(433,60,'SUBTOTAL: ')
    bill.drawString(450,45,'TOTAL: ')
    bill.setFont('Helvetica', size=8)

    bill.drawString(500, 75, str(variables.lblfacturas[11].get_text()))
    bill.drawString(500, 60, str(variables.lblfacturas[10].get_text()))
    bill.drawString(500,45,str(variables.lblfacturas[9].get_text()))



def listacli():
    try:

        global bill
        bill = canvas.Canvas('listaclientes.pdf', pagesize=A4)
        basico()
        cabeceralistacli()
        cuerpolistacli()
        bill.save()
        bill.showPage()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/listaclientes.pdf')
    except:
        print('Error impimir listacli')

def cabeceralistacli():
    bill.setFont('Helvetica-Bold', size=8)
    text = 'Nombre de empresa:'
    bill.drawString(50, 735, text)

    bill.setFont('Helvetica', size=8)
    text2 = 'Hotel Lite'
    bill.drawString(140, 735,text2)

    bill.setFont('Helvetica-Bold', size=8)
    text3 = 'Telefono'
    bill.drawString(320, 735, text3)

    bill.setFont('Helvetica', size=8)
    text4 = '986000000000'
    bill.drawString(400, 735, text4)

    bill.setFont('Helvetica-Bold', size=8)
    text5 = 'Dirección:'
    bill.drawString(50, 710, text5)

    bill.setFont('Helvetica', size=8)
    text6 = 'Calle inventada viva python'
    bill.drawString(120, 710, text6)

    bill.setFont('Helvetica-Bold', size=8)
    text6 = 'E-mail:'
    bill.drawString(320, 710, text6)

    bill.setFont('Helvetica', size=8)
    text7 = 'info@hotelite.com'
    bill.drawString(400, 710, text7)

    bill.setFont('Helvetica-Bold', size=8)
    text8 = 'Sitio web:'
    bill.drawString(50, 685, text8)

    bill.setFont('Helvetica', size=8)
    text9 = 'https://www.hotelite.com'
    bill.drawString(120, 685,text9)

    bill.setFont('Helvetica-Bold', size=10)
    text = ['CODIGO', 'DNI', 'NOMBRE', 'APELLIDOS','DATA']
    x = 60

    bill.drawString(x, 649, text[0])
    x=x+60
    bill.drawString(x, 649, text[1])
    x=x+70
    bill.drawString(x, 649, text[2])
    x=x+140

    bill.drawString(x, 649, text[3])
    x=x+120

    bill.drawString(x, 649, text[4])

    bill.line(50,635,540,635)



def cuerpolistacli():


    lista = funcionescli.listar()
    print(len(lista))
    x=65
    con =0
    y=615

    while con!=len(lista):
        bill.setFont('Helvetica', size=8)
        bill.drawString(x, y, str(lista[con][0]))
        x=x+60
        bill.drawString(x, y, str(lista[con][1]))
        x=x+70
        bill.drawString(x, y, str(lista[con][2]))
        x=x+140
        bill.drawString(x, y, str(lista[con][3]))
        x=x+120
        bill.drawString(x, y, str(lista[con][4]))
        y=y-20
        x=65
        con = con +1
        if con%25==0:
            try:
                bill.showPage()
                basico()
                cabeceralistacli()

                x=65
                y=615
            except:
                print('Error salto de pag')

    x=x+390


