# -*- coding: utf-8 -*-
#
#	AUTHOR: TOLO VICH LOZANO 
#
#	DESCRIPTION:
#		Very simple program for diferential copy with rsync
#		You need to have rsync installed and Pyside
#
#
# Created: Wed Aug 19 09:09:34 2015
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import os
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
	
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 145)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 79, 29))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 85, 29))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(105, 20, 380, 29))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(105, 50, 380, 29))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 20, 111, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 50, 111, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(105, 90, 111, 29))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 90, 111, 29))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
	def openDirectoryDialog():
		
        	"""
        	Opens a dialog for choose a directory
        	"""
        	
        	d1 = directory = QtGui.QFileDialog.getExistingDirectory()
        	                                                       
        	self.lineEdit.setText(d1)
	def openDirectoryDialog2():
		
        	"""
        	Opens a dialog for choose a directory
        	"""
        	
        	d2 = directory = QtGui.QFileDialog.getExistingDirectory()
        	                                                       
        	self.lineEdit_2.setText(d2)

	def copiar():

		a = self.lineEdit.text()
		b = self.lineEdit_2.text()
		c = "rsync -av --progress "+a+" "+b		
		os.system(c)		


        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), lambda:openDirectoryDialog())
	QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), lambda:openDirectoryDialog2())
	QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), copiar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simple Py Sync", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "RUN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MainWindow()
    self.ui.setupUi(self)
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
sys.exit(app.exec_())
