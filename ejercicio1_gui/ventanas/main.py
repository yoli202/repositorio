
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal , ventana_insertar, ventana_listar
import sys



def mostrar_registro_prenda():
    ui_insertar_prenda.setupUi(MainWindow)
def mostrar_listado_prenda():
    ui_listar_prenda.setupUi(MainWindow)
def mostrar_inicio():
    ui.setupUi(MainWindow)
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui_insertar_prenda = ventana_insertar.Ui_MainWindow()
ui_listar_prenda = ventana_listar.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.submenu_insertar_prenda.triggered.connect(mostrar_registro_prenda)
ui.submenu_listar_prenda.triggered.connect(mostrar_listado_prenda)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
    
MainWindow.show()
sys.exit(app.exec_())
