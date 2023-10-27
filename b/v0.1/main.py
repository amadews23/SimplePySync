import subprocess

from PySide2 import QtCore, QtGui, QtWidgets
import os
import sys

from PySide2.QtWidgets import QFileDialog, QDialog, QMessageBox

import dialogo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 675) #225
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 79, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 79, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_file_source = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file_source.setGeometry(QtCore.QRect(80, 10, 411, 29))
        self.lineEdit_file_source.setObjectName("lineEdit_file_source")
        self.lineEdit_file_source.setReadOnly(True)

        self.lineEdit_file_dest = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file_dest.setGeometry(QtCore.QRect(80, 50, 411, 29))
        self.lineEdit_file_dest.setObjectName("lineEdit_file_dest")
        self.lineEdit_file_dest.setReadOnly(True)

        self.pushButton_file_source = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file_source.setGeometry(QtCore.QRect(500, 10, 111, 29))
        self.pushButton_file_source.setObjectName("pushButton_file_source")

        self.pushButton_file_dest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file_dest.setGeometry(QtCore.QRect(500, 50, 111, 29))
        self.pushButton_file_dest.setObjectName("pushButton_file_dest")

        self.checkBox_delete_dest = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_delete_dest.setGeometry(QtCore.QRect(80, 90, 440, 40))
        self.checkBox_delete_dest.setText("Borrar archivos en destino si no están en origen (--delete)")

        self.pushButton_sync = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sync.setGeometry(QtCore.QRect(80, 130, 111, 29))
        self.pushButton_sync.setObjectName("pushButton_sync")

        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(380, 130, 111, 29))
        self.pushButton_close.setObjectName("pushButton_close")

        self.output_term = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_term.setGeometry(QtCore.QRect(10, 170, 600, 444))
        self.output_term.setObjectName("output_term")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        fichero_config = open('pysync.conf', "r")
        ruta_origen = str(fichero_config.readline())


        if os.path.exists(ruta_origen.strip()):
          self.lineEdit_file_source.setText(ruta_origen.strip())

        ruta_destino = str(fichero_config.readline())
        if os.path.exists(ruta_destino.strip()):
          self.lineEdit_file_dest.setText(ruta_destino.strip())

        def open_directory_dialog(line_edit, titulo, ruta):
            """
            Opens a dialog for choose a directory
            """
            d = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                           titulo,
                                                           ruta,
                                                           QFileDialog.ShowDirsOnly)
            """
            If the directory is not selected, the lineEdit does not change
            """
            if d != "":
                line_edit.setText(d)

        def copiar():

            a = ""
            b = self.lineEdit_file_source.text()
            c = self.lineEdit_file_dest.text()

            if len(self.lineEdit_file_dest.text()) == 0:
                dialogo.show_dialogo("Advertencia", "Seleccione una carpeta de destino")

            if self.lineEdit_file_source.text() == self.lineEdit_file_dest.text():
                dialogo.show_dialogo("Advertencia", "La carpeta de origen es igual a la carpeta de destino")

            if len(self.lineEdit_file_dest.text()) != 0 and \
                    self.lineEdit_file_source.text() != self.lineEdit_file_dest.text():

                self.pushButton_sync.setDisabled(True)
                self.pushButton_file_dest.setDisabled(True)
                self.pushButton_file_source.setDisabled(True)

                if self.checkBox_delete_dest.isChecked():
                    a = " --delete "

                print("Copiando....")

                if os.name == 'posix':
                    comando = "rsync -av --progress " + a + b + " " + c

                if os.name == 'nt':
                    winformat = "\\"
                    unixformat = "/"
                    dospuntos = ":"
                    nada = ""
                    b = b.replace(dospuntos, nada)
                    c = c.replace(dospuntos, nada)
                    b = b.replace(winformat, unixformat)
                    c = c.replace(winformat, unixformat)
                    comando = "rsync -av --progress " + a + '"' + "/cygdrive/" + b + '"' + " " + '"' + "/cygdrive/" + c + '"'

                #print(comando)
                #os.system(comando)
                resultado = subprocess.check_output(comando, shell=True)

                self.output_term.setText(comando+"\n"+"\n"+resultado.decode("utf-8") )
                print("Fin")

                self.pushButton_sync.setDisabled(False)
                self.pushButton_file_dest.setDisabled(False)
                self.pushButton_file_source.setDisabled(False)

        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_file_source, QtCore.SIGNAL("clicked()"),
                               lambda: open_directory_dialog(self.lineEdit_file_source, "Selecciona carpeta de origen", ruta_origen))
        QtCore.QObject.connect(self.pushButton_file_dest, QtCore.SIGNAL("clicked()"),
                               lambda: open_directory_dialog(self.lineEdit_file_dest, "Selecciona carpeta de destino", ruta_destino))
        QtCore.QObject.connect(self.pushButton_sync, QtCore.SIGNAL("clicked()"), copiar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Sync"))
        self.label.setText(_translate("MainWindow", "Origen"))
        self.label_2.setText(_translate("MainWindow", "Destino"))
        self.pushButton_file_source.setText(_translate("MainWindow", "Seleccionar"))
        self.pushButton_file_dest.setText(_translate("MainWindow", "Seleccionar"))
        self.pushButton_sync.setText(_translate("MainWindow", "Ejecutar"))
        self.pushButton_close.setText(_translate("MainWindow", "Salir"))


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
sys.exit(app.exec_())
