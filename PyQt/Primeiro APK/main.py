from PyQt6 import uic, QtWidgets

import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)

App = QtWidgets.QApplication([])
window = uic.loadUi(resource_path('style.ui'))

window.show()
App.exec()

