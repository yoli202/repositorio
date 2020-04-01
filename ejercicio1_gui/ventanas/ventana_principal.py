# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_ventana_principal = QtWidgets.QLabel(self.centralwidget)
        self.label_ventana_principal.setGeometry(QtCore.QRect(170, 170, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label_ventana_principal.setFont(font)
        self.label_ventana_principal.setObjectName("label_ventana_principal")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuropa = QtWidgets.QMenu(self.menubar)
        self.menuropa.setObjectName("menuropa")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_insertar_prenda = QtWidgets.QAction(MainWindow)
        self.submenu_insertar_prenda.setObjectName("submenu_insertar_prenda")
        self.submenu_listar_prenda = QtWidgets.QAction(MainWindow)
        self.submenu_listar_prenda.setObjectName("submenu_listar_prenda")
        self.submenu_inicio = QtWidgets.QAction(MainWindow)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.menuropa.addAction(self.submenu_insertar_prenda)
        self.menuropa.addAction(self.submenu_listar_prenda)
        self.menuropa.addAction(self.submenu_inicio)
        self.menubar.addAction(self.menuropa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ventana_principal.setText(_translate("MainWindow", "Bienvenido a mi Tienda \n"
" de Moda"))
        self.menuropa.setTitle(_translate("MainWindow", "ropa"))
        self.submenu_insertar_prenda.setText(_translate("MainWindow", "insertar_prenda"))
        self.submenu_listar_prenda.setText(_translate("MainWindow", "listar_prenda"))
        self.submenu_inicio.setText(_translate("MainWindow", "inicio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
