from PyQt6 import uic, QtWidgets
import webbrowser


import sys
from os.path import join, abspath
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)


def menu_azul():
    tela.label_2.setText('Azul')
    tela.label_2.setStyleSheet('color:#0000D9;font-size:25px;font-weight:bold;')

def menu_amarelo():
    tela.label_2.setText('Amarelo')
    tela.label_2.setStyleSheet('color:#FFBF00;font-size:25px;font-weight:bold;')

def menu_vermelho():
    tela.label_2.setText('Vermelho')
    tela.label_2.setStyleSheet('color:#FF0000;font-size:25px;font-weight:bold;')

def menu_verde():
    tela.label_2.setText('Verde')
    tela.label_2.setStyleSheet('color:#2DB200;font-size:25px;font-weight:bold;')

def menu_limpar():
    tela.label_2.setText('Preto')
    tela.label_2.setStyleSheet('color:#000;font-size:25px;font-weight:bold;')

def menu_sobre():
    webbrowser.open('http://muller.nocciolli.com.br')


app = QtWidgets.QApplication([])
tela = uic.loadUi(resource_path('menu.ui'))

tela.actionAzul.triggered.connect(menu_azul)
tela.actionAmarelo.triggered.connect(menu_amarelo)
tela.actionVermelho.triggered.connect(menu_vermelho)
tela.actionVerde.triggered.connect(menu_verde)
tela.actionLimpar.triggered.connect(menu_limpar)
tela.actionNocciolli.triggered.connect(menu_sobre)


tela.show()
app.exec()