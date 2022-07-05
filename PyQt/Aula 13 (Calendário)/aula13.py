import PyQt5


from PyQt6 import uic, QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

def pegar_data():
    data = str(tela.calendarWidget.selectedDate())
    data = data[19:31].replace('(','').replace(')','').replace(' ','')
    data = data.split(',')
    data = data[2]+'/'+data[1]+'/'+data[0]
    tela.label_2.setText(data)

app = QtWidgets.QApplication([])
tela = uic.loadUi(resource_path('aula13.ui'))

tela.calendarWidget.selectionChanged.connect(pegar_data)

tela.show()
app.exec()