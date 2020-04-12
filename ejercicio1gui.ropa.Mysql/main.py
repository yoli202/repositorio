
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal #importamos todo lo que hay en el paquete ventanas
from ventanas import ventana_insertar, ventana_listar,\
ventana_list_widget, ventana_table_widget
import sys
from modelo.clases import Prenda
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidget, QTableWidgetItem, QPushButton
from _functools import partial

#variable con el resultado de base de datos:
lista_resultado=None

#inicio funciones

def registrar_prenda():
    prenda = Prenda()
    prenda.prenda = ui_registrar.insertar_prenda.text()
    prenda.talla = ui_registrar.insertar_talla.text()
    prenda.color = ui_registrar.insertar_color.text()
    prenda.temporada = ui_registrar.insertar_temporada.text()
    prenda.precio = ui_registrar.insertar_precio.text()
    operaciones_bd.registro_ropa(prenda)
    QMessageBox.about(MainWindow,"Info","Registro de prenda ok")


def mostrar_registro_prenda():
    ui_registrar.setupUi(MainWindow)
    ui_registrar.boton_registrar_prenda.clicked.connect(registrar_prenda)

def mostrar_listar_prenda():
    ui_listar.setupUi(MainWindow)
    lista_resultado=operaciones_bd.obtener_ropa()
    texto = ""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " prenda: " + str(l[1]) + " talla: " + str(l[2]) + " color: " + str(l[3]) + " temporada: " + str(l[4]) + " precio: " +str(l[5]) + "\n"
    ui_listar.listar_prenda.setText(texto)


def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_ropa()
    #voy a rellenar el list widget
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_prenda.addItem( " prenda: " + str(l[1])+ " talla: " + str(l[2]) + " color: " + str(l[3]) + " temporada: " + str(l[4]) + " precio: " +str(l[5]) + "\n")
    
    ui_ventana_list_widget.list_widget_prenda.itemClicked.connect(mostrar_registro)

#funcion que hace algo, en este caso mostrar toda la informacion cuando se haga clik en un registro
#elemento del
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_prenda.currentRow()
    texto= ""
    texto += "prenda: " + str(lista_resultado[indice_seleccionado][1]) + "\n"
    texto += "talla: " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += "color: " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += "temporada: " + str(lista_resultado[indice_seleccionado][4]) + "\n"
    texto += "precio: " + str(lista_resultado[indice_seleccionado][5])

    QMessageBox.about(MainWindow,"INFO", texto)

#funciones para la tabla:
def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
#vamos a rellenar la tabla:
    ropa = operaciones_bd.obtener_ropa()
    fila = 0
    for l in ropa:
        ui_ventana_table_widget.table_ropa.insertRow(fila)
        columna_indice = 0
        for valor in l:
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.table_ropa.setItem(fila,columna_indice,celda)
            columna_indice += 1
        #despues de rellenar los datos en la fila
        #voy a meter un boton para borrar 
        boton_borrar = QPushButton("borrar")
        boton_borrar.clicked.connect(partial(borrar_ropa,l[0]))
        ui_ventana_table_widget.table_ropa.setCellWidget(fila,6,boton_borrar)
        fila += 1
        
def borrar_ropa(id):
    res = QMessageBox.question(MainWindow, "Info", " Vas a borrar un registro de id:"+ str(id))
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_ropa(id)
        mostrar_table_widget()

        #celda para el id
        #celda = QTableWidgetItem(str(l[0]))
        #ui_ventana_table_widget.table_ropa.setItem(fila,0,celda)
        #celda para el nombre:
        #celda = QTableWidgetItem(str(l[1]))
        #ui_ventana_table_widget.table_ropa.setItem(fila,1,celda)
        #celda para las paginas:
        #celda = QTableWidgetItem(str(l[2]))
        #ui_ventana_table_widget.table_ropa.setItem(fila,2,celda)
#celda para el precio:
        #celda = QTableWidgetItem(str(l[3]))
        #ui_ventana_table_widget.table_ropa.setItem(fila,3,celda)
        #celda = QTableWidgetItem(str(l[4]))
        #ui_ventana_table_widget.table_ropa.setItem(fila,4,celda)
        #celda = QTableWidgetItem(str(l[5]))
        #ui_ventana_table_widget.table_ropa.setItem(fila,5,celda)
        

def mostrar_inicio():
    ui.setupUi(MainWindow)

#fin definicion funciones
app = QtWidgets.QApplication(sys.argv) #linea obligatoria para usar pyqt5
MainWindow = QtWidgets.QMainWindow()#crear una ventana principal con pyqt5

ui = ventana_principal.Ui_MainWindow()#creo el interfaz definido por ventana principal.py
#es el archivo generado desde la consola a partir del archivo de diseño ventana_principal.ui

ui_registrar = ventana_insertar.Ui_MainWindow() #lo mismo para registrar libro
ui_listar = ventana_listar.Ui_MainWindow() #lo mismo para listar libros
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()

ui.setupUi(MainWindow)#todo lo que tiene el interfaz de la ventana principal lo pongo en el
#MainWindow

#asignar las funciones a los submenus from ventanas import ventana_registrar_libro, ventana_listado_libros
ui.submenu_insertar_prenda.triggered.connect(mostrar_registro_prenda)
ui.submenu_listar_prenda.triggered.connect(mostrar_listar_prenda)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
ui.submenu_list_widget.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget.triggered.connect(mostrar_table_widget)

MainWindow.show() #Mostrar la ventana_principal de pyqt5
sys.exit(app.exec_()) #cerrar la aplicacion cuando se cierre la ventana