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
        MainWindow.resize(749, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 60, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listar_prenda = QtWidgets.QTextEdit(self.centralwidget)
        self.listar_prenda.setGeometry(QtCore.QRect(50, 150, 651, 401))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listar_prenda.setFont(font)
        self.listar_prenda.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.listar_prenda.setObjectName("listar_prenda")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Listado de prendas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
