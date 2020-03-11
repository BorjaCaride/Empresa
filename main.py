#coding=utf-8
"""
El main contiene los elementos necesarios para lanzar la aplicación
así como la declaración de los widgets que se usarán. También los módulos
que tenemos que importar de las librerías gráficas.

"""
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import funcionescli, funcioneshab, funcionesreser,funcionesvar,funcioneservicios
import eventos,conexion,variables


class Empresa:
    def __init__(self):
        """
        Cargamos los widgets con algún evente asociado o que son referenciados

        """
        self.b = Gtk.Builder()
        self.b.add_from_file('ventana.glade')


        vprincipal = self.b.get_object('venPrincipal')
        self.vendialog = self.b.get_object('venDialog')
        variables.vendialogexportar = self.b.get_object('venDialogExportar')
        variables.vendialogimportar = self.b.get_object('venDialogImportar')
        variables.vendialoghabocupada = self.b.get_object('venDialogHabOcupada')
        variables.vendialogfactura = self.b.get_object('venDialogFactura')
        variables.venacercade = self.b.get_object('venAcercade')
        variables.panel = self.b.get_object('Panel')
        variables.filechooserbackup = self.b.get_object('fileChooserbackup')
        menubar = self.b.get_object('menuBar').get_style_context()

        entdni = self.b.get_object('entDni')
        entapel = self.b.get_object('entApel')
        entnome = self.b.get_object('entNome')
        entdatacli = self.b.get_object('entDatacli')
        lblerrdni = self.b.get_object('lblErrdni')
        lblcodcli = self.b.get_object('lblCodcli')
        lblnumnoches = self.b.get_object('lblNumnoches')
        lbldirbackup = self.b.get_object('lblFolderbackup')
        lbldnires = self.b.get_object('lblDnires')
        lblapelres = self.b.get_object('lblApelres')
        lblfacdni = self.b.get_object('lblFacDni')
        lblfacapel = self.b.get_object('lblFacApel')
        lblfaccodres = self.b.get_object('lblFacCodRes')
        lblfacnome = self.b.get_object('lblFacNome')
        lblfachab = self.b.get_object('lblFacHab')
        lblfaccon = self.b.get_object('lblFacCon')
        lblfaccon2 = self.b.get_object('lblFacCon2')
        lblfaccon3 = self.b.get_object('lblFacCon3')
        lblfaccon4 = self.b.get_object('lblFacCon4')
        lblfaccon5 = self.b.get_object('lblFacCon5')
        lblfacunid = self.b.get_object('lblFacUnid')
        lblfacunid2 = self.b.get_object('lblFacUnid2')
        lblfacunid3 = self.b.get_object('lblFacUnid3')
        lblfacunid4 = self.b.get_object('lblFacUnid4')
        lblfacunid5 = self.b.get_object('lblFacUnid5')
        lblfacprecio = self.b.get_object('lblFacPrecioU')
        lblfacprecio2 = self.b.get_object('lblFacPrecioU2')
        lblfacprecio3 = self.b.get_object('lblFacPrecioU3')
        lblfacprecio4 = self.b.get_object('lblFacPrecioU4')
        lblfacprecio5 = self.b.get_object('lblFacPrecioU5')
        lblfactotal = self.b.get_object('lblFacTotal')
        lblfactotal2 = self.b.get_object('lblFacTotal2')
        lblfactotal3 = self.b.get_object('lblFacTotal3')
        lblfactotal4 = self.b.get_object('lblFacTotal4')
        lblfactotal5 = self.b.get_object('lblFacTotal5')
        totalfactura = self.b.get_object('totalfactura')
        subtotal = self.b.get_object('lblSubTotal')
        iva = self.b.get_object('lblIva')
        variables.conceptofac = (lblfaccon,lblfaccon2,lblfaccon3,lblfaccon4,lblfaccon5)
        variables.unidadfac = (lblfacunid,lblfacunid2,lblfacunid3,lblfacunid4,lblfacunid5)
        variables.preciofac = (lblfacprecio,lblfacprecio2,lblfacprecio3,lblfacprecio4,lblfacprecio5)
        variables.totalfac = (lblfactotal,lblfactotal2,lblfactotal3,lblfactotal4,lblfactotal5)
        variables.lblfacturas = (lblfacdni, lblfacapel, lblfacnome, lblfaccodres, lblfachab, variables.conceptofac, variables.unidadfac , variables.preciofac, variables.totalfac,totalfactura,subtotal,iva)
        variables.vencalendar = self.b.get_object('venCalendar')
        variables.vendialogsalir = self.b.get_object('vendialogSalir')
        variables.calendar = self.b.get_object('Calendar')
        variables.filacli = (entdni, entapel, entnome, entdatacli)
        variables.listclientes = self.b.get_object('listClientes')
        variables.treereservas = self.b.get_object('treeReservas')
        variables.listreservas = self.b.get_object('listReservas')
        variables.treeclientes = self.b.get_object('treeClientes')
        variables.menslabel = (lblerrdni, lblcodcli, lblnumnoches, lbldirbackup, lbldnires, lblapelres)

        entnumhab = self.b.get_object('entNumhab')
        entprezohab = self.b.get_object('entPrezohab')
        rbtsimple = self.b.get_object('rbtSimple')
        rbtdoble = self.b.get_object('rbtDoble')
        rbtfamily = self.b.get_object('rbtFamily')
        variables.treehab = self.b.get_object('treeHab')
        variables.listhab = self.b.get_object('listHab')
        variables.filahab = (entnumhab, entprezohab)
        variables.filarbt = (rbtsimple, rbtdoble, rbtfamily)
        variables.listcmbhab = self.b.get_object('listcmbHab')
        variables.cmbhab = self.b.get_object('cmbNumres')
        variables.switch = self.b.get_object('switch')


        entdatain = self.b.get_object('entDatain')
        entdataout = self.b.get_object('entDataout')

        variables.filareserva = (entdni, entapel, entdatain, entdataout)

        lblcodres = self.b.get_object('lblCodReservaServ')
        lblnumhab = self.b.get_object('lblHabitacionServ')
        rbtnsa = self.b.get_object('rbtnSA')
        rbtncomida = self.b.get_object('rbtnComida')
        rbtndesyuno = self.b.get_object('rbtnDesayuno')
        cbparking = self.b.get_object('cbParking')
        variables.datosserv = (lblcodres,lblnumhab)
        variables.filarbtnser = (rbtnsa,rbtndesyuno,rbtncomida,cbparking)
        entnomserv = self.b.get_object('entNomServ')
        entprecioserv = self.b.get_object('entPrecioServ')
        variables.nuevoser = (entnomserv,entprecioserv)
        variables.treeserv = self.b.get_object('treeServicios')
        variables.listserv = self.b.get_object('listServ')



        self.b.connect_signals(eventos.Eventos())


        self.set_style()
        menubar.add_class('menuBar')
        '''
        for i in range(len(variables.menserror)):
            variables.menserror[i].add_class('label')
        '''
        vprincipal.show_all()
        vprincipal.maximize()
        conexion.Conexion().abrirbbdd()
        funcionesreser.listadores()
        funcioneshab.listadonumhab(self)
        funcionescli.listadocli(variables.listclientes)
        funcioneshab.listadohab(variables.listhab)

        funcionesvar.controlhab()


    def set_style(self):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('estilos.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__=='__main__':
    main = Empresa()
    Gtk.main()

