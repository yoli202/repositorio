from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal 
import sys


def convertir_de_euros_a_yen_japones():
  
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    yen_japones = introducido_float * 0.0085
    ui.label_resultado.setText("en yen japones : " + "{:.2f}".format(yen_japones).replace(".",","))
    
def convertir_de_euros_a_pesos():
  
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    pesos = introducido_float * 26.54
    ui.label_resultado.setText("en pesos: " + "{:.2f}".format(pesos).replace(".",","))
    
def convertir_de_euros_a_libras():
  
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    libras = introducido_float * 0.88
    ui.label_resultado.setText("en libras: " + "{:.2f}".format(libras).replace(".",","))
    
def convertir_de_euros_a_dolar():
  
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    dolar = introducido_float * 0.92
    ui.label_resultado.setText("en dolar: " + "{:.2f}".format(dolar).replace(".",","))
    
def convertir_de_euros_a_franco_suizo():
  
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    franco_suizo = introducido_float * 1.06
    ui.label_resultado.setText("en franco suizo : " + "{:.2f}".format(franco_suizo).replace(".",","))
    
    
    
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.boton_yen_japones.clicked.connect(convertir_de_euros_a_yen_japones)
ui.boton_pesos.clicked.connect(convertir_de_euros_a_pesos)
ui.boton_libras.clicked.connect(convertir_de_euros_a_libras)
ui.boton_dolar.clicked.connect(convertir_de_euros_a_dolar)
ui.boton_franco_suizo.clicked.connect(convertir_de_euros_a_franco_suizo)

MainWindow.show()
sys.exit(app.exec_())
