import sys
from PyQt6 import uic, QtWidgets, QtTest
from PyQt6.QtCore import Qt

from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)


def progress():
    i = 5
    for i in range(101):
        if i == 100:
            tela.progressBar.setValue(i)
            tela.destroy()
            tela2.show()
        else:
            tela.progressBar.setValue(i)
            QtTest.QTest.qWait(20)

if __name__ == '__main__':
    App = QtWidgets.QApplication([])

    tela = uic.loadUi(resource_path('main.ui'))
    tela.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    tela.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    tela2 = uic.loadUi(resource_path('window.ui'))

    tela.show()
    progress()

    sys.exit(App.exec())