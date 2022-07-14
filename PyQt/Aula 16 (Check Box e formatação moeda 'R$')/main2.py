from PyQt6 import uic, QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

def calcular():
    soma = float(0.00)
    if (window.checkBox.isChecked()):
        soma += 1500.00
    if (window.checkBox_2.isChecked()):
        soma += 20.00
    if (window.checkBox_3.isChecked()):
        soma += 10.00
    if (window.checkBox_4.isChecked()):
        soma += 32.00
    if (window.checkBox_5.isChecked()):
        soma += 5.50

    window.label_2.setText(f'R$ {soma:_.2f}'.replace('.',',').replace('_','.'))

App = QtWidgets.QApplication([])
window = uic.loadUi(resource_path('checkbox2.ui'))
window.checkBox.stateChanged.connect(calcular)
window.checkBox_2.stateChanged.connect(calcular)
window.checkBox_3.stateChanged.connect(calcular)
window.checkBox_4.stateChanged.connect(calcular)
window.checkBox_5.stateChanged.connect(calcular)

window.show()
App.exec()
