
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal #importamos todo lo que hay en el paquete ventanas
from ventanas import ventana_insertar, ventana_listar,\
ventana_list_widget, ventana_table_widget, ventana_editar
import sys
from modelo.clases import Prenda
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidget, QTableWidgetItem, QPushButton, QPixmap   
from _functools import partial
from validadores import validadores_prenda
from PyQt5.QtWidgets import QFileDialog
import shutil  #para copiar archivo digital imagen





#variable con el resultado de base de datos:
lista_resultado=None

#inicio funciones

def registrar_prenda():
    prenda = Prenda()
    prenda.prenda = ui_registrar.insertar_prenda.text()
    prenda.prenda = prenda.prenda.strip()#elimina espacios en blanco
    # asi validamos libro
    resultado_validar_prenda = validadores_prenda.validar_prenda(prenda.prenda)
    if resultado_validar_prenda == None :
        ui_registrar.label_error_prenda.setText("<font color='red'> Error en Prenda</font")
        return
    else:
        ui_registrar.label_error_prenda.clear()
    prenda.talla = ui_registrar.insertar_talla.text()
    prenda.talla = prenda.talla.strip()#elimina espacios en blanco
    # asi validamos libro
    resultado_validar_talla = validadores_prenda.validar_talla(prenda.talla)
    if resultado_validar_talla == None :
        ui_registrar.label_error_talla.setText("<font color='red'> Error en Talla</font")
        return
    else:
        ui_registrar.label_error_talla.clear()
    
    prenda.color = ui_registrar.insertar_color.text()
    prenda.color = prenda.color.strip()#elimina espacios en blanco
    # asi validamos libro
    resultado_validar_color = validadores_prenda.validar_color(prenda.color)
    if resultado_validar_color == None :
        ui_registrar.label_error_color.setText("<font color='red'> Error en Color</font")
        return
    else:
        ui_registrar.label_error_color.clear()
        
    prenda.temporada = ui_registrar.insertar_temporada.text()
    prenda.temporada = prenda.temporada.strip()#elimina espacios en blanco
    # asi validamos libro
    resultado_validar_temporada = validadores_prenda.validar_temporada(prenda.temporada)
    if resultado_validar_temporada == None :
        ui_registrar.label_error_temporada.setText("<font color='red'> Error en Temporada</font")
        return
    else:
        ui_registrar.label_error_temporada.clear()
    prenda.precio = ui_registrar.insertar_precio.text()
    prenda.precio = prenda.precio.strip()#elimina espacios en blanco
    
    # checbox
    if ui_registrar.CheckBox_digital.isChecked():
        prenda.digital = True
    #combo
    indice_seleccionado = ui_registrar.combo_tipo.currentIndex()
    prenda.tipo = ui_registrar.combo_tipo.itemText(indice_seleccionado)
    #radio
    if ui_registrar.radio_standar.isChecked():
        prenda.envio = "standar"
    
    if ui_registrar.radio_urgente.isChecked():
        prenda.envio = "urgente"
    
    if ui_registrar.radio_prioritario.isChecked():
        prenda.envio = "prioritario"
    
    operaciones_bd.registro_ropa(prenda)
    QMessageBox.about(MainWindow,"Info","Registro de prenda ok")

def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo, "temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    ancho_label_imagen = ui_registrar.label_imagen.width()
    pixmap_redim = pixmap.scaledToWidth(ancho_label_imagen)
    ui_registrar.label_imagen.setPixmap(pixmap_redim)
    
    
    
def mostrar_registro_prenda():
    ui_registrar.setupUi(MainWindow)
    ui_registrar.boton_registrar_prenda.clicked.connect(registrar_prenda)
    ui_registrar.boton_seleccionar_imagen.clicked.connect(seleccionar_imagen)
    ui_registrar.label_error_prenda.clear()#elimina el texto
    ui_registrar.label_error_talla.clear()
    ui_registrar.label_error_color.clear()
    ui_registrar.label_error_temporada.clear()
    ui_registrar.label_error_precio.clear()

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
            if columna_indice == 6:
                if valor == 0:
                    valor = "NO"
                else:
                    valor = "SI"
            celda = QTableWidgetItem(str(valor))
            ui_ventana_table_widget.table_ropa.setItem(fila,columna_indice,celda)
            columna_indice += 1
        #despues de rellenar los datos en la fila
        #voy a meter un boton para borrar 
        boton_borrar = QPushButton("borrar")
        boton_borrar.clicked.connect(partial(borrar_ropa,l[0]))
        ui_ventana_table_widget.table_ropa.setCellWidget(fila,9,boton_borrar)
        
        boton_editar = QPushButton("editar")
        boton_editar.clicked.connect(partial(editar_prenda, l[0]))
        ui_ventana_table_widget.table_ropa.setCellWidget(fila,10,boton_editar)
        fila += 1

def editar_prenda(id):
    QMessageBox.about(MainWindow,"Info", "vas a editar un registro id:" + str(id))
    ui_ventana_editar.setupUi(MainWindow)
    #sacar de base de datos toda la informacion a editar
    prenda_a_editar = operaciones_bd.obtener_prenda_por_id(id)
    ui_ventana_editar.insertar_prenda.setText(prenda_a_editar.prenda)
    ui_ventana_editar.label_error_prenda.clear()
    ui_ventana_editar.insertar_talla.setText(str(prenda_a_editar.talla))
    ui_ventana_editar.label_error_talla.clear()
    ui_ventana_editar.insertar_color.setText(str(prenda_a_editar.color))
    ui_ventana_editar.label_error_color.clear()
    ui_ventana_editar.insertar_temporada.setText(str(prenda_a_editar.temporada))
    ui_ventana_editar.label_error_temporada.clear()
    ui_ventana_editar.insertar_precio.setText(str(prenda_a_editar.precio))
    
    
    if prenda_a_editar.digital:
        ui_ventana_editar.CheckBox_digital.setChecked(True)
    # combo
    ui_ventana_editar.combo_tipo.setCurrentText(prenda_a_editar.tipo)
    # CheckBox
    if prenda_a_editar.envio == "standar":
        ui_ventana_editar.radio_standar.setChecked(True)
    if prenda_a_editar.envio == "urgente":
        ui_ventana_editar.radio_urgente.setChecked(True)
    if prenda_a_editar.envio == "prioritario":
        ui_ventana_editar.radio_prioritario.setChecked(True)
        
    ui_ventana_editar.boton_guardar_cambios_prenda.clicked.connect(partial(guardar_cambios_prenda,prenda_a_editar.id))

def guardar_cambios_prenda(id):
    QMessageBox.about(MainWindow,"Info","guardar cambios sobre el registro de id: " + str(id))
    prenda_guardar_cambios = Prenda()
    prenda_guardar_cambios.prenda = ui_ventana_editar.insertar_prenda.text()
    
    resultado_validar_prenda = validadores_prenda.validar_prenda(prenda_guardar_cambios.prenda)
    if resultado_validar_prenda == None :
        ui_ventana_editar.label_error_prenda.setText("<font color='red'> Inserta Prenda</font")
        return
    else:
        ui_ventana_editar.label_error_prenda.clear()
        
    prenda_guardar_cambios.talla = ui_ventana_editar.insertar_talla.text()
    
    resultado_validar_prenda = validadores_prenda.validar_talla(prenda_guardar_cambios.talla)
    if resultado_validar_prenda == None :
        ui_ventana_editar.label_error_talla.setText("<font color='red'> Inserta Talla </font")
        return
    else:
        ui_ventana_editar.label_error_talla.clear()
        
    prenda_guardar_cambios.color = ui_ventana_editar.insertar_color.text()
    
    resultado_validar_prenda = validadores_prenda.validar_color(prenda_guardar_cambios.color)
    if resultado_validar_prenda == None :
        ui_ventana_editar.label_error_color.setText("<font color='red'> Inserta Color </font")
        return
    else:
        ui_ventana_editar.label_error_color.clear()
   
    
    prenda_guardar_cambios.temporada = ui_ventana_editar.insertar_temporada.text()
    resultado_validar_prenda = validadores_prenda.validar_temporada(prenda_guardar_cambios.temporada)
    if resultado_validar_prenda == None :
        ui_ventana_editar.label_error_temporada.setText("<font color='red'> Inserta Temporada </font")
        return
    else:
        ui_ventana_editar.label_error_temporada.clear()
    
    
    prenda_guardar_cambios.precio = ui_ventana_editar.insertar_precio.text()
    
    if ui_ventana_editar.CheckBox_digital.isChecked():
        prenda_guardar_cambios.digital = True
    prenda_guardar_cambios.tipo = ui_ventana_editar.combo_tipo.currentText()
    if ui_ventana_editar.radio_standar.isChecked():
        prenda_guardar_cambios.envio = "standar"
    if ui_ventana_editar.radio_urgente.isChecked():
        prenda_guardar_cambios.envio = "urgente"
    if ui_ventana_editar.radio_prioritario.isChecked():
        prenda_guardar_cambios.envio = "prioritario"
    prenda_guardar_cambios.id = id
    operaciones_bd.guardar_cambios_prenda(prenda_guardar_cambios)
    mostrar_table_widget()#vuelvo a mostrar todos los libros

        
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
ui_ventana_editar = ventana_editar.Ui_MainWindow()

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