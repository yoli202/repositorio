# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_insertar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 600)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_precio = QtWidgets.QLabel(self.centralwidget)
        self.label_precio.setGeometry(QtCore.QRect(40, 220, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_precio.setFont(font)
        self.label_precio.setObjectName("label_precio")
        self.insertar_talla = QtWidgets.QLineEdit(self.centralwidget)
        self.insertar_talla.setGeometry(QtCore.QRect(150, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.insertar_talla.setFont(font)
        self.insertar_talla.setObjectName("insertar_talla")
        self.insertar_color = QtWidgets.QLineEdit(self.centralwidget)
        self.insertar_color.setGeometry(QtCore.QRect(150, 130, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.insertar_color.setFont(font)
        self.insertar_color.setObjectName("insertar_color")
        self.insertar_temporada = QtWidgets.QLineEdit(self.centralwidget)
        self.insertar_temporada.setGeometry(QtCore.QRect(150, 180, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.insertar_temporada.setFont(font)
        self.insertar_temporada.setObjectName("insertar_temporada")
        self.insertar_precio = QtWidgets.QLineEdit(self.centralwidget)
        self.insertar_precio.setGeometry(QtCore.QRect(150, 230, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.insertar_precio.setFont(font)
        self.insertar_precio.setObjectName("insertar_precio")
        self.boton_registrar_prenda = QtWidgets.QPushButton(self.centralwidget)
        self.boton_registrar_prenda.setGeometry(QtCore.QRect(40, 460, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.boton_registrar_prenda.setFont(font)
        self.boton_registrar_prenda.setObjectName("boton_registrar_prenda")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.insertar_prenda = QtWidgets.QLineEdit(self.centralwidget)
        self.insertar_prenda.setGeometry(QtCore.QRect(150, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.insertar_prenda.setFont(font)
        self.insertar_prenda.setObjectName("insertar_prenda")
        self.CheckBox_digital = QtWidgets.QCheckBox(self.centralwidget)
        self.CheckBox_digital.setGeometry(QtCore.QRect(420, 310, 70, 17))
        self.CheckBox_digital.setObjectName("CheckBox_digital")
        self.combo_tipo = QtWidgets.QComboBox(self.centralwidget)
        self.combo_tipo.setGeometry(QtCore.QRect(550, 310, 69, 22))
        self.combo_tipo.setObjectName("combo_tipo")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.label_precio_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_precio_2.setGeometry(QtCore.QRect(60, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_precio_2.setFont(font)
        self.label_precio_2.setObjectName("label_precio_2")
        self.radio_standar = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_standar.setGeometry(QtCore.QRect(240, 310, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_standar.setFont(font)
        self.radio_standar.setChecked(True)
        self.radio_standar.setAutoRepeat(False)
        self.radio_standar.setObjectName("radio_standar")
        self.radio_urgente = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_urgente.setGeometry(QtCore.QRect(240, 350, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_urgente.setFont(font)
        self.radio_urgente.setObjectName("radio_urgente")
        self.radio_prioritario = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_prioritario.setGeometry(QtCore.QRect(240, 390, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radio_prioritario.setFont(font)
        self.radio_prioritario.setObjectName("radio_prioritario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 310, 31, 16))
        self.label.setObjectName("label")
        self.label_error_prenda = QtWidgets.QLabel(self.centralwidget)
        self.label_error_prenda.setGeometry(QtCore.QRect(440, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_error_prenda.setFont(font)
        self.label_error_prenda.setObjectName("label_error_prenda")
        self.label_error_talla = QtWidgets.QLabel(self.centralwidget)
        self.label_error_talla.setGeometry(QtCore.QRect(440, 80, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_error_talla.setFont(font)
        self.label_error_talla.setObjectName("label_error_talla")
        self.label_error_color = QtWidgets.QLabel(self.centralwidget)
        self.label_error_color.setGeometry(QtCore.QRect(440, 130, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_error_color.setFont(font)
        self.label_error_color.setObjectName("label_error_color")
        self.label_error_temporada = QtWidgets.QLabel(self.centralwidget)
        self.label_error_temporada.setGeometry(QtCore.QRect(440, 180, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_error_temporada.setFont(font)
        self.label_error_temporada.setObjectName("label_error_temporada")
        self.label_error_precio = QtWidgets.QLabel(self.centralwidget)
        self.label_error_precio.setGeometry(QtCore.QRect(440, 240, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_error_precio.setFont(font)
        self.label_error_precio.setObjectName("label_error_precio")
        self.label_precio_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_precio_3.setGeometry(QtCore.QRect(300, 430, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_precio_3.setFont(font)
        self.label_precio_3.setObjectName("label_precio_3")
        self.boton_seleccionar_imagen = QtWidgets.QPushButton(self.centralwidget)
        self.boton_seleccionar_imagen.setGeometry(QtCore.QRect(300, 490, 121, 23))
        self.boton_seleccionar_imagen.setObjectName("boton_seleccionar_imagen")
        self.label_imagen = QtWidgets.QLabel(self.centralwidget)
        self.label_imagen.setGeometry(QtCore.QRect(490, 382, 211, 171))
        self.label_imagen.setText("")
        self.label_imagen.setObjectName("label_imagen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Talla:"))
        self.label_3.setText(_translate("MainWindow", "Color:"))
        self.label_4.setText(_translate("MainWindow", "Temporada:"))
        self.label_precio.setText(_translate("MainWindow", "Precio:"))
        self.boton_registrar_prenda.setText(_translate("MainWindow", "Registrar prenda"))
        self.label_5.setText(_translate("MainWindow", "Prenda:"))
        self.CheckBox_digital.setText(_translate("MainWindow", "Digital"))
        self.combo_tipo.setItemText(0, _translate("MainWindow", "chico"))
        self.combo_tipo.setItemText(1, _translate("MainWindow", "chica"))
        self.label_precio_2.setText(_translate("MainWindow", "Opciones de envio:"))
        self.radio_standar.setText(_translate("MainWindow", "Envio Standar"))
        self.radio_urgente.setText(_translate("MainWindow", "Envio Urgente"))
        self.radio_prioritario.setText(_translate("MainWindow", "Envio Prioritario"))
        self.label.setText(_translate("MainWindow", "Tipo"))
        self.label_error_prenda.setText(_translate("MainWindow", "Insertar Prenda"))
        self.label_error_talla.setText(_translate("MainWindow", "Insertar Talla"))
        self.label_error_color.setText(_translate("MainWindow", "Insertar Color"))
        self.label_error_temporada.setText(_translate("MainWindow", "Insertar Temporada"))
        self.label_error_precio.setText(_translate("MainWindow", "Insertar Precio"))
        self.label_precio_3.setText(_translate("MainWindow", "Imagenes:"))
        self.boton_seleccionar_imagen.setText(_translate("MainWindow", "Seleccionar imagen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
