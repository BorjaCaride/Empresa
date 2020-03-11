#coding=utf-8
"""
Módulo que gestiona todos los eventos

"""

import gi
import xlrd
import xlwt

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import conexion, variables, funcionescli, funcioneshab, funcionesreser, funcionesvar, facturacion, impresion,funcioneservicios
import os, shutil


class Eventos():
    """
      Clase que tiene todos los eventos
      """

    def on_acercade_activate(self, widget):
        """
        Gestiona el botón Acerca de.
        Abre la ventana Acerca de
        :param widget:
        :return: No devuelve nada

        """
        try:
            variables.venacercade.show()
        except:
            print('error abrira acerca de')

    def on_btnCerrarabout_clicked(self, widget):
        """
        Gestiona el evento para cerrar correctamente la ventada Acerca de.
        Cierra la ventana Acerca de.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.venacercade.connect('delete-event', lambda w, e: w.hide() or True)
            variables.venacercade.hide()
        except:
            print('error abrir calendario')
    def on_btnAceptarsalirI_clicked(self,widget):
        """
        Gestiona el boton salir de la ventana importar.
        Función que sirve para cerrar correctamente la ventada de Importar.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.vendialogimportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vendialogimportar.hide()
        except:
            print('Erro cerrar ventana importar')
    def on_btnAceptarsalirE_clicked(self,widget):
        """
        Gestiona el boton salir de la ventana Exportar.
        Función que sirve para cerrar correctamente la ventada de Exportar.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.vendialogexportar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vendialogexportar.hide()
        except:
            print('Erro cerrar ventana exportar')

    def on_btnAceptarsalirHab_clicked(self,widget):
        """
        Gestiona el boton salir de la ventana Habitación ocupada.
        Función que sirve para cerrar correctamente la ventada de Habitación ocupada.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.vendialoghabocupada.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vendialoghabocupada.hide()
        except:
            print('Erro cerrar ventana habitacion ocupada')
    def on_btnAceptarsalirFactura_clicked(self,widget):
        try:
            variables.vendialogfactura.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vendialogfactura.hide()
        except:
            print('Erro cerrar ventana habitacion ocupada')

    def on_menuBarsalir_activate(self, widget):
        """
        Gestiona el boton salir de la barra de menú.
        Función que sirve para cerrar la aplicación correctamente.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            self.salir()
        except:
            print('salir en menubar')

    def salir(self):
        """
        Metodo para cerrar la aplicacion y la base de datos.
        :return: No devuelve nada.

        """
        try:
            conexion.Conexion.cerrarbbdd(self)
            funcionesvar.cerrartimer()
            Gtk.main_quit()
        except:
            print('error función salir')

    def on_venPrincipal_destroy(self, widget):
        """
        Gestiona el evento para cerrar la aplicacion correctamente
        Cierra la aplicacion correctamente.
        :param widget:
        :return: No devuelve nada.

        """
        self.salir()

    def on_btnSalirtool_clicked(self, widget):
        """
        Gestiona el evento del botón Salir de la barra de herramientas.
        Muestra la ventana de pregunta.
        :param widget:
        :return: No devuelve nada.

        """
        variables.vendialogsalir.show()

    def on_btnCancelarsalir_clicked(self, widget):
        """
        Gestiona el evento del boton cancelar de la ventana de salir de la aplicación.
        Cancela el cierre de la aplicación
        :param widget:
        :return: No devuelve nada

        """
        variables.vendialogsalir.connect('delete-event', lambda w, e: w.hide() or True)
        variables.vendialogsalir.hide()

    def on_btnAceptarsalir_clicked(self, widget):
        """
        Gestiona el boton aceptar de la ventana de salir de la aplicación.
        Cierra la aplicacion.
        :param widget:
        :return:No devuelve nada.

        """
        self.salir()

    def on_btnAltacli_clicked(self, widget):
        """
        Gestiona el evento del botón de alta cliente.
        Da de alta un cliente
        :param widget:
        :return: No devuelve nada

        """
        try:
            dni = variables.filacli[0].get_text()
            apel = variables.filacli[1].get_text()
            nome = variables.filacli[2].get_text()
            data = variables.filacli[3].get_text()
            registro = (dni, apel, nome, data)
            if funcionescli.validoDNI(dni):
                funcionescli.insertarcli(registro)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                variables.menslabel[0].set_text('ERROR DNI')
        except:
            print("Error alta cliente")


    def on_btnBajacli_clicked(self, widget):
        """
        Gestiona el evento del botón de baja cliente.
        Da de baja un cliente.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            dni = variables.filacli[0].get_text()
            if dni != '':
                funcionescli.bajacli(dni)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                print('falta dni u otro error')
        except:
            print("error en botón baja cliente")

    def on_btnModifcli_clicked(self, widget):
        """
        Gestiona el evento del botón modificar de la ventana de clientes.
        Modifica un cliente
        :param widget:
        :return: No devuelve nada.

        """
        try:
            cod = variables.menslabel[1].get_text()
            dni = variables.filacli[0].get_text()
            apel = variables.filacli[1].get_text()
            nome = variables.filacli[2].get_text()
            data = variables.filacli[3].get_text()
            registro = (dni, apel, nome, data)
            if dni != '':
                funcionescli.modifcli(registro, cod)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                print('falta el dni')
        except:
            print('error en botón modificar')

    def on_entDni_focus_out_event(self, widget, dni):
        """
        Valida el dni.
        :param widget:
        :param dni: Contiene el dni del cliente.
        :return:No devuelve nada.

        """
        try:
            dni = variables.filacli[0].get_text()
            if funcionescli.validoDNI(dni):
                variables.menslabel[0].set_text('')
                pass
            else:
                variables.menslabel[0].set_text('ERROR')
        except:
            print("Error alta cliente en out focus")

    def on_treeClientes_cursor_changed(self, widget):
        """
        Gestionar la accion de cuando se haga click en un cliente en el treeview.
        Carga en los entrys los datos del cliente seleccionado.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            model, iter = variables.treeclientes.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            variables.menslabel[0].set_text('')
            funcionescli.limpiarentry(variables.filacli)
            if iter != None:
                sdni = model.get_value(iter, 0)
                sapel = model.get_value(iter, 1)
                snome = model.get_value(iter, 2)
                sdata = model.get_value(iter, 3)
                if sdata == None:
                    sdata = ''
                cod = funcionescli.selectcli(sdni)
                variables.menslabel[1].set_text(str(cod[0]))
                variables.filacli[0].set_text(str(sdni))
                variables.filacli[1].set_text(str(sapel))
                variables.filacli[2].set_text(str(snome))
                variables.filacli[3].set_text(str(sdata))
                variables.menslabel[4].set_text(str(sdni))
                variables.menslabel[5].set_text(str(sapel))
        except:
            print("error carga cliente")

    def on_btnCalendar_clicked(self, widget):
        """
        Gestiona el evento del boton calendario de la ventana de clientes.
        Muestra una ventana con un calendario.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.semaforo = 1
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()

        except:
            print('error abrir calendario')

    def on_btnCalendarResIn_clicked(self, widget):
        """
        Gestiona el evento del botón calendario de la ventana de reservas.
        Muestra una ventana con un calendario.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.semaforo = 2
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()
        except:
            print('error abrir calendario')

    def on_btnCalendarResOut_clicked(self, widget):
        """
        Gestiona el evento del botón calendario de la ventana de reservas.
        Muestra una ventana con un calendario.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.semaforo = 3
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()
        except:
            print('error abrir calendario')

    def on_Calendar_day_selected_double_click(self, widget):
        """
        Gestiona el evento de doble click en el calendario.
        Recoge la fecha.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            agno, mes, dia = variables.calendar.get_date()
            fecha = "%02d/" % dia + "%02d/" % (mes + 1) + "%s" % agno
            if variables.semaforo == 1:
                variables.filacli[3].set_text(fecha)
            elif variables.semaforo == 2:
                variables.filareserva[2].set_text(fecha)
            elif variables.semaforo == 3:
                variables.filareserva[3].set_text(fecha)
                funcionesreser.calculardias()
            else:
                pass
            variables.vencalendar.hide()
        except:
            print('error al coger la fecha')



    def on_btnAltahab_clicked(self, widget):
        """
        Gestiona el evento del botón alta de la ventana de habitaciones.
        Da de alta una nueva habitación.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            numhab = variables.filahab[0].get_text()
            prezohab = variables.filahab[1].get_text()
            prezohab = prezohab.replace(',', '.')
            prezohab = float(prezohab)
            prezohab = round(prezohab, 2)
            if variables.filarbt[0].get_active():
                tipo = 'simple'
            elif variables.filarbt[1].get_active():
                tipo = 'doble'
            elif variables.filarbt[2].get_active():
                tipo = 'family'
            else:
                pass

            if variables.switch.get_active():
                libre = 'SI'
            else:
                libre = 'NO'
            registro = (numhab, tipo, prezohab, libre)
            if numhab != None:
                funcioneshab.insertarhab(registro)
                funcioneshab.listadohab(variables.listhab)
                funcioneshab.listadonumhab()
                funcioneshab.limpiarentry(variables.filahab)
            else:
                pass
        except:
            print("Error alta habitacion")



    def on_treeHab_cursor_changed(self, widget):
        """
        Gestionar la accion de cuando se haga click en una habitación en el treeview.
        Carga en los entrys los datos de la habitación seleccionada.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            model, iter = variables.treehab.get_selection().get_selected()
            funcioneshab.limpiarentry(variables.filahab)
            if iter != None:
                snumhab = model.get_value(iter, 0)
                stipo = model.get_value(iter, 1)
                sprezo = model.get_value(iter, 2)
                sprezo = round(sprezo, 2)
                variables.filahab[0].set_text(str(snumhab))
                variables.filahab[1].set_text(str(sprezo))
                if stipo == str('simple'):
                    variables.filarbt[0].set_active(True)
                elif stipo == str('doble'):
                    variables.filarbt[1].set_active(True)
                elif stipo == str('family'):
                    variables.filarbt[2].set_active(True)
                slibre = model.get_value(iter, 3)
                if slibre == str('SI'):
                    variables.switch.set_active(True)
                else:
                    variables.switch.set_active(False)
        except:
            print("error carga habitacion")

    def on_btnBajahab_clicked(self, widget):
        """
        Gestiona el botón de baja en la ventana de habitaciones.
        Da de baja una habitación.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            numhab = variables.filahab[0].get_text()
            if numhab != '':
                funcioneshab.bajahab(numhab)
                funcioneshab.limpiarentry(variables.filahab)
                funcioneshab.listadohab(variables.listhab)
            else:
                pass
        except:
            print('borrar baja hab')

    def on_btnModifhab_clicked(self, widget):
        """
        Gestiona el botón modificar en la ventana de habitaciones.
        Modifica una habitación.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            numhab = variables.filahab[0].get_text()
            prezo = variables.filahab[1].get_text()
            if variables.switch.get_active():
                libre = 'SI'
            else:
                libre = 'NO'

            if variables.filarbt[0].get_active():
                tipo = 'simple'
            elif variables.filarbt[1].get_active():
                tipo = 'doble'
            elif variables.filarbt[2].get_active():
                tipo = 'family'
            else:
                pass
            registro = (prezo, tipo, libre)
            if numhab != '':
                funcioneshab.modifhab(registro, numhab)
                funcioneshab.listadohab(variables.listhab)
                funcioneshab.limpiarentry(variables.filahab)
            else:
                print('falta el numhab')
        except:
            print('error modif hab')


    def on_Panel_select_page(self, widget):
        try:
            funcioneshab.listadonumhab()
        except:
            print("error botón cliente barra herramientas")

    def on_btnClitool_clicked(self, widget):
        """
        Gestiona el evento de ir a ventana clientes de la barra de herramientas.
        Comprueba en que ventana esta y se mueve a la ventana de clientes.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 0:
                variables.panel.set_current_page(0)
            else:
                pass
        except:
            print("error botón cliente barra herramientas")

    def on_btnReservatool_clicked(self, widget):
        """
        Gestiona el evento de ir a ventana reservas de la barra de herramientas.
        Comprueba en que ventana esta y se mueve a la ventana de reservas.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 1:
                variables.panel.set_current_page(1)
                funcioneshab.listadonumhab(self)
            else:
                pass
        except:
            print("error botón cliente barra herramientas")

    def on_btnHabita_clicked(self, widget):
        """
        Gestiona el evento de ir a ventana habitaciones de la barra de herramientas.
        Comprueba en que ventana esta y se mueve a la ventana de habitaciones.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 2:
                variables.panel.set_current_page(2)
            else:
                pass
        except:
            print("error botón habitacion barra herramientas")

    def on_btnServtool_clicked(self,widget):
        """
        Gestiona el evento de ir a ventana de servicios de la barra de herramientas.
        Comprueba en que ventana esta y se mueve a la ventana de servicios.
        :param widget:
        :return: No devuelve nada
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 3:
                variables.panel.set_current_page(3)
            else:
                pass
        except:
            print("error botón servicios barra herramientas")

    def on_btnCalc_clicked(self, widget):
        """
        Gestiona el evento del botón calculadora.
        Habre una nueva ventana con la calculadora.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            os.system('/snap/bin/gnome-calculator')
        except:
            print('error lanzar calculadora')

    def on_btnRefresh_clicked(self, widget):
        """
        Gestiona el evento de refresh.
        Limpia todos los entry y los label.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            funcioneshab.limpiarentry(variables.filahab)
            funcionescli.limpiarentry(variables.filacli)
            funcionesreser.limpiarentry(variables.filareserva)
            facturacion.limpiarfactura()
            facturacion.limpiardatosclifactura()
        except:
            print('error referes')

    def on_btnBackup_clicked(self, widget):
        """
        Gestiona el evento del botón backup.
        Restaura una copia de seguridad.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.filechooserbackup.show()
            variables.neobackup = funcionesvar.backup()
            variables.neobackup = str(os.path.abspath(variables.neobackup))
            print(variables.neobackup)

        except:
            print('error abrir file choorse backup')

    def on_btnGrabarbackup_clicked(self, widget):
        """
        Gestiona el evento del botón guardar backup.
        Hace una copia de seguridad.
        :param widget:
        :return:No devuelve nada.

        """
        try:
            destino = variables.filechooserbackup.get_filename()
            destino = destino + '/'
            variables.menslabel[3].set_text(str(destino))
            if shutil.move(str(variables.neobackup), str(destino)):
                variables.menslabel[3].set_text('Copia de Seguridad Creada')
        except:
            print('error dselect fichero')

    def on_btnCancelfilechooserbackup_clicked(self, widget):
        """
        Gestiona el evento del botón cancelar de la ventana de elegir archivo para resturar.
        Cierra la fentana.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.filechooserbackup.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserbackup.hide()
        except:
            print('error cerrar file chooser')



    def on_cmbNumres_changed(self, widget):
        """
        Gestiona el combobox de la ventana de habitaciones.
        Muestra las habitaciones en el combobox.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            index = variables.cmbhab.get_active()
            model = variables.cmbhab.get_model()
            item = model[index]
            variables.numhabres = item[0]
        except:
            print('error mostrar habitacion combo')

    def on_btnAltares_clicked(self, widget):
        """
        Gestiona el evento del botón alta de la ventana de reservas
        Da de alta una nueva reserva.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            if variables.reserva == 1:
                dnir = variables.menslabel[4].get_text()
                chki = variables.filareserva[2].get_text()
                chko = variables.filareserva[3].get_text()
                noches = int(variables.menslabel[2].get_text())
                registro = (dnir, variables.numhabres, chki, chko, noches)
                if funcionesreser.versilibre(variables.numhabres):
                    funcionesreser.insertares(registro)
                    funcionesreser.listadores()
                    # actualizar a NO
                    libre = ['NO']
                    funcioneshab.cambiaestadohab(libre, variables.numhabres,0)
                    funcioneshab.listadohab(variables.listhab)
                    funcioneshab.limpiarentry(variables.filahab)
                    funcionesreser.limpiarentry(variables.filareserva)
                else:
                    variables.vendialoghabocupada.show()
        except:
            print('error en alta res')

    def on_btnRefreshcmbhab_clicked(self, widget):
        """
        Gestiona el evento de refresh del combobox de la ventana de habitaciones.
        :param widget:
        :return: No devuelve nada.

        """
        try:
            variables.cmbhab.set_active(-1)
            funcioneshab.listadonumhab(self)
        except:
            print('error limpiar combo hotel')

    def on_treeReservas_cursor_changed(self, widget):
        """
        Gestionar la acción de cuando se haga click en una reserva en el treeview
        Carga los datos en los entrys de la ventana de reservas
        :param widget:
        :return: No devuelve nada.

        """
        try:
            model, iter = variables.treereservas.get_selection().get_selected()
            facturacion.limpiarfactura()
            if iter != None:
                variables.codr = model.get_value(iter, 0)
                sdni = model.get_value(iter, 1)
                sapel = funcionesreser.buscarapelcli(str(sdni))
                snome = funcionesreser.buscarnomecli(str(sdni))
                snumhab = model.get_value(iter, 2)
                sprezo = funcionesreser.buscarpreciohab(str(snumhab))
                lista = funcioneshab.listadonumhabres()

                variables.lblfacturas[0].set_text(str(sdni))
                variables.lblfacturas[1].set_text(str(sapel[0]))
                variables.lblfacturas[2].set_text(str(snome[0]))
                variables.lblfacturas[3].set_text(str(variables.codr))
                variables.lblfacturas[4].set_text(str(snumhab))

                m = -1
                for i, x in enumerate(lista):
                    if str(x[0]) == str(snumhab):
                        m = i
                variables.cmbhab.set_active(m)
                schki = model.get_value(iter, 3)
                schko = model.get_value(iter, 4)
                snoches = model.get_value(iter, 5)
                variables.menslabel[4].set_text(str(sdni))
                variables.menslabel[5].set_text(str(sapel[0]))
                variables.menslabel[2].set_text(str(snoches))
                variables.filareserva[2].set_text(str(schki))
                variables.filareserva[3].set_text(str(schko))

                variables.lblfacturas[5][0].set_text(str('Noches'))
                variables.lblfacturas[6][0].set_text(str(snoches))
                variables.lblfacturas[7][0].set_text(str(sprezo[0]))
                variables.total = facturacion.calcprezo(float(sprezo[0]), float(snoches))
                variables.lblfacturas[8][0].set_text(str(variables.total))
                variables.datosserv[0].set_text(str(variables.codr))
                variables.datosserv[1].set_text(snumhab)
                total = facturacion.cargardatos(variables.total)
                subtotal = variables.lblfacturas[10].get_text()
                iva = variables.lblfacturas[11].get_text()
                global datosfactura
                datosfactura = (sdni, sapel[0], snome[0], snumhab, sprezo, schko, str(variables.codr),str(total),str(subtotal),str(iva))
                if(funcioneservicios.comprobar(variables.codr)!=0):
                    funcioneservicios.listadoserv(variables.codr)


        except:
            print('error cargar valores de reservas')

    def on_btnBajares_clicked(self, widget):
        """
        Gestiona el evento del botón baja de la ventana de reservas.
        Da de baja una reserva
        :param widget:
        :return: No devuelve nada.
        """
        try:
            funcionesreser.bajareserva(variables.codr)
            libre ="SI"
            funcioneshab.cambiaestadohab(libre,variables.numhabres,1)
            funcioneshab.listadohab(variables.listhab)
            funcionesreser.limpiarentry(variables.filareserva)
            funcionesreser.listadores()

        except:
            print('error baja reserva')

    def on_btnImprimirFac_clicked(self, widget):
        try:

            impresion.factura(datosfactura)
        except:
            variables.vendialogfactura.show()
            print('No sale el modulo de impresion')



    def on_btnImprimirCli_clicked(self,widget):
        """
        Imprimir listado de clientes
        :param widget:
        :return:
        """

        try:
            impresion.listacli()

        except:
            print('No sale el modulo de impresion de clientes')
        pass

    def on_menuBarExportar_activate(self,widget):
        """
        Gestiona el evento del botón exportar de la barra de menú.
        Se encarga de leer todos los clientes y escribirlso en un documento xls.
        :param widget:
        :return: No devuelve nada.

        """
        style0 =xlwt.easyxf('font: name DejaVu Sans')
        wb =xlwt.Workbook()

        lista = funcionescli.listar()
        con=0

        ws = wb.add_sheet('NuevoClientes', cell_overwrite_ok=True)
        while con != len(lista):
            ws.write(con, 0, lista[con][1], style0)
            ws.write(con, 1, lista[con][2], style0)
            ws.write(con, 2, lista[con][3], style0)
            ws.write(con, 3, lista[con][4], style0)
            con=con + 1
        wb.save('exportarclientes.xls')
        variables.vendialogexportar.show()

    def on_menuBarImportar_activate(self,widget):
        """
        Gestiona el evento del botón importar de la barra de menú.
        Obtiene clientes, a partir de un fichero xlsx, y los almacena en la base de datos.
        :param widget:
        :return: No devuelve nada.

        """
        document = xlrd.open_workbook("listadoclientes.xlsx")
        clientes=document.sheet_by_index(0)
        todo = 0
        for i in range(clientes.nrows-1):
            for j in range(clientes.ncols):
                if i !=0:
                    if j == 0:
                        dni = str(clientes.cell_value(i,0))
                        apel = str(clientes.cell_value(i, 1))
                        nome = str(clientes.cell_value(i,2))
                        data = float(clientes.cell_value(i,3))
                        year, mont, d, h, m, s = xlrd.xldate_as_tuple(data, 0)
                        dia = str(d)
                        mes =str(mont)
                        ano = str(year)
                        fecha = dia.zfill(2)+'/'+mes.zfill(2)+'/'+ano
                        registro = (dni,apel,nome,fecha)
                        if(funcionescli.selectcli(dni)==None):
                            funcionescli.insertarcli(registro)
                            funcionescli.listadocli(variables.listclientes)
                            funcionescli.limpiarentry(variables.filacli)
                            todo = 1
        if todo == 1:
            variables.vendialogimportar.show()




    def on_btnAltaServNuevo_clicked(self,widget):
        """
        Gestiona el evento del botón alta servicio adicional de la ventana de servicios
        Da de alta un nuevo servicio.
        :param widget:
        :return:No devuelve nada

        """
        try:
            codresr = variables.datosserv[0].get_text()
            nomservicio = variables.nuevoser[0].get_text()
            precio = variables.nuevoser[1].get_text()
            registro = (codresr,nomservicio,precio)

            if nomservicio!="" and codresr!="" and precio!="":
                funcioneservicios.insertarserv(registro)

                funcioneservicios.listadoserv(codresr)
                funcioneservicios.limpiarentry(variables.nuevoser)
                facturacion.cargardatos(variables.total)
            else:
                print('Faltan datos')
        except:
            print('Error alta servicio')



    def on_treeServicios_cursor_changed(self,widget):
        """
        Gestionar la accion de cuando se haga click en un servicio en el treeview
        :param widget:
        :return:No devuelve nada.

        """
        model, iter = variables.treeserv.get_selection().get_selected()
        if iter !=None:
            sconcepto = model.get_value(iter,1)
            sprecio = model.get_value(iter,2)
            if str(sconcepto)=="Desayuno":
                variables.filarbtnser[1].set_active(True)
            elif str(sconcepto)=="Comida":
                variables.filarbtnser[2].set_active(True)
            elif str(sconcepto)=="Parking":
                variables.filarbtnser[3].set_active(True)
            variables.nuevoser[0].set_text(str(sconcepto))
            variables.nuevoser[1].set_text(str(sprecio))

    def on_btnAltaServ_clicked(self,widget):
        """
        Gestiona el botón alta de la ventana servicio.
        :param widget:
        :return: No devuelve nada.

        """
        codresr = variables.datosserv[0].get_text()

        parking = 'Parking'
        if variables.filarbtnser[0].get_active():
            facturacion.borrardatos()
            funcioneservicios.servicioSA(codresr)
        else:
            if variables.filarbtnser[1].get_active():
                nomservicio = 'Desayuno'
            elif variables.filarbtnser[2].get_active():
                nomservicio ='Comida'
            precio = funcioneservicios.verprecio(nomservicio)
            registro = (codresr, str(nomservicio), precio[0][0])
            listaa = funcioneservicios.comprobarservicio(codresr)
            con =0
            i = 0
            while con != len(listaa):
                if listaa[con]==nomservicio:
                    i = 1
                con = con+1
            if i !=1:
                funcioneservicios.insertarserv(registro)
            else:
                print('Valor ya introducido')


        if variables.filarbtnser[3].get_active():
            precio = funcioneservicios.verprecio(parking)
            registro = (codresr, str(parking), precio[0][0])
            funcioneservicios.insertarserv(registro)


        funcioneservicios.listadoserv(codresr)
        facturacion.cargardatos(variables.total)

    def on_btnBajaServicio_clicked(self,widget):
        """
        Gestiona el evento del botón baja servicio adicional de la ventana de servicios
        :param widget:
        :return: No devuelve nada.

        """
        try:
            model, iter = variables.treeserv.get_selection().get_selected()
            cod = model.get_value(iter,0)
            concepto = model.get_value(iter,1)
            if str(concepto)=="Parking":
                variables.filarbtnser[3].set_active(False)
            facturacion.borrardatos()
            funcioneservicios.bajaservicio(cod)
            facturacion.cargardatos(variables.total)
            funcioneservicios.listadoserv(variables.codr)
            funcioneservicios.limpiarentry(variables.nuevoser)
        except:
            print('Error alta servicio')


