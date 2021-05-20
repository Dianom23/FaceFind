from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("test.ui")
ui.show()
app.exec()