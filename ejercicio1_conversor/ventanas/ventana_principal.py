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
        MainWindow.resize(747, 598)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 70, 341, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_resultado_yen = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado_yen.setGeometry(QtCore.QRect(480, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_resultado_yen.setFont(font)
        self.label_resultado_yen.setText("")
        self.label_resultado_yen.setObjectName("label_resultado_yen")
        self.label_resultado_franco = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado_franco.setGeometry(QtCore.QRect(490, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_resultado_franco.setFont(font)
        self.label_resultado_franco.setText("")
        self.label_resultado_franco.setObjectName("label_resultado_franco")
        self.boton_yen_japones = QtWidgets.QPushButton(self.centralwidget)
        self.boton_yen_japones.setGeometry(QtCore.QRect(130, 160, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.boton_yen_japones.setFont(font)
        self.boton_yen_japones.setObjectName("boton_yen_japones")
        self.boton_franco_suizo = QtWidgets.QPushButton(self.centralwidget)
        self.boton_franco_suizo.setGeometry(QtCore.QRect(270, 310, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.boton_franco_suizo.setFont(font)
        self.boton_franco_suizo.setObjectName("boton_franco_suizo")
        self.boton_dolar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_dolar.setGeometry(QtCore.QRect(420, 240, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.boton_dolar.setFont(font)
        self.boton_dolar.setObjectName("boton_dolar")
        self.boton_pesos = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pesos.setGeometry(QtCore.QRect(430, 160, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.boton_pesos.setFont(font)
        self.boton_pesos.setObjectName("boton_pesos")
        self.boton_libras = QtWidgets.QPushButton(self.centralwidget)
        self.boton_libras.setGeometry(QtCore.QRect(130, 240, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.boton_libras.setFont(font)
        self.boton_libras.setObjectName("boton_libras")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(260, 400, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(550, 79, 113, 31))
        self.entrada_euros.setObjectName("entrada_euros")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CONVERSOR DE MONEDAS A EUROS"))
        self.boton_yen_japones.setText(_translate("MainWindow", "CONVERTIR  EN YEN JAPONES"))
        self.boton_franco_suizo.setText(_translate("MainWindow", "CONVERTIR  EN FRANCO SUIZO"))
        self.boton_dolar.setText(_translate("MainWindow", "CONVERTIR  EN DOLAR"))
        self.boton_pesos.setText(_translate("MainWindow", "CONVERTIR  EN PESOS"))
        self.boton_libras.setText(_translate("MainWindow", "CONVERTIR  EN LIBRAS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
