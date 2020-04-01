# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_mostrar_catalogo = QtWidgets.QPushButton(self.centralwidget)
        self.boton_mostrar_catalogo.setGeometry(QtCore.QRect(124, 80, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(18)
        self.boton_mostrar_catalogo.setFont(font)
        self.boton_mostrar_catalogo.setObjectName("boton_mostrar_catalogo")
        self.label_listado = QtWidgets.QLabel(self.centralwidget)
        self.label_listado.setGeometry(QtCore.QRect(26, 180, 691, 411))
        self.label_listado.setText("")
        self.label_listado.setObjectName("label_listado")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_mostrar_catalogo.setText(_translate("MainWindow", "mostrar catalogo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
