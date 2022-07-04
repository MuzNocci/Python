from PyQt6 import uic, QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

def chama():
    window2.show()

def trocatexto():
    window2.label.setText('Hello World!!!')

App = QtWidgets.QApplication([])
window1 = uic.loadUi(resource_path('aula11_win1.ui'))
window2 = uic.loadUi(resource_path('aula11_win2.ui'))
window1.pushButton.clicked.connect(chama)
window2.pushButton_2.clicked.connect(trocatexto)

window1.show()
App.exec()

