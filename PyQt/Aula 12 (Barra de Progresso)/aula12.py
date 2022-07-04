from PyQt6 import uic, QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

valor = 0

def aumentar():
    global valor
    valor = valor+10
    window.progressBar.setValue(valor)

def zerar():
    global valor
    valor = 0
    window.progressBar.setValue(valor)

App = QtWidgets.QApplication([])
window = uic.loadUi(resource_path('aula12.ui'))
window.pushButton.clicked.connect(aumentar)
window.pushButton_2.clicked.connect(zerar)

window.show()
App.exec()

