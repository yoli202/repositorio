# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1258, 598)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_ropa = QtWidgets.QTableWidget(self.centralwidget)
        self.table_ropa.setGeometry(QtCore.QRect(70, 130, 1101, 431))
        self.table_ropa.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.table_ropa.setObjectName("table_ropa")
        self.table_ropa.setColumnCount(11)
        self.table_ropa.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_ropa.setHorizontalHeaderItem(10, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 50, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_ropa.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table_ropa.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "prenda"))
        item = self.table_ropa.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "talla"))
        item = self.table_ropa.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "color"))
        item = self.table_ropa.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "temporada"))
        item = self.table_ropa.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "precio"))
        item = self.table_ropa.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "digital"))
        item = self.table_ropa.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "tipo"))
        item = self.table_ropa.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "envio"))
        item = self.table_ropa.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "borrar"))
        item = self.table_ropa.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "editar"))
        self.label.setText(_translate("MainWindow", "TABLA DE ROPA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
