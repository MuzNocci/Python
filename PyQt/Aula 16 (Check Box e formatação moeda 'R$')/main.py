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
        window.checkBox.setChecked(False)
        soma += 1500.00
    if (window.checkBox_2.isChecked()):
        window.checkBox_2.setChecked(False)
        soma += 20.00
    if (window.checkBox_3.isChecked()):
        window.checkBox_3.setChecked(False)
        soma += 10.00
    if (window.checkBox_4.isChecked()):
        window.checkBox_4.setChecked(False)
        soma += 32.00
    if (window.checkBox_5.isChecked()):
        window.checkBox_5.setChecked(False)
        soma += 5.50

    window.label_2.setText(f'R$ {soma:_.2f}'.replace('.',',').replace('_','.'))

App = QtWidgets.QApplication([])
window = uic.loadUi(resource_path('checkbox.ui'))
window.pushButton.clicked.connect(calcular)

window.show()
App.exec()
