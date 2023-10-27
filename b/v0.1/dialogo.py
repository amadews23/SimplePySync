from PySide2.QtWidgets import QMessageBox


def show_dialogo(titulo="Titulo", mensaje="Mensaje"):
    dlg = QMessageBox()
    dlg.setWindowTitle(titulo)
    dlg.setText(mensaje)
    dlg.setStandardButtons(QMessageBox.Ok)
    dlg.setIcon(QMessageBox.Question)
    button = dlg.exec_()
