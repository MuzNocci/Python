# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setStyleSheet(u"background-color:rgb(85, 170, 255);")
        self.actionAzul = QAction(mainWindow)
        self.actionAzul.setObjectName(u"actionAzul")
        self.actionAmarelo = QAction(mainWindow)
        self.actionAmarelo.setObjectName(u"actionAmarelo")
        self.actionVermelho = QAction(mainWindow)
        self.actionVermelho.setObjectName(u"actionVermelho")
        self.actionVerde = QAction(mainWindow)
        self.actionVerde.setObjectName(u"actionVerde")
        self.actionLimpar = QAction(mainWindow)
        self.actionLimpar.setObjectName(u"actionLimpar")
        self.actionNocciolli = QAction(mainWindow)
        self.actionNocciolli.setObjectName(u"actionNocciolli")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 371, 51))
        self.label.setStyleSheet(u"font-size:25px;font-weight:bold;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 80, 761, 481))
        self.frame.setStyleSheet(u"background-color:#fff;border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 201, 31))
        self.label_2.setStyleSheet(u"font-size:25px; font-weight:bold;color:black;")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menubar.setTabletTracking(False)
        self.menuCores = QMenu(self.menubar)
        self.menuCores.setObjectName(u"menuCores")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        mainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuCores.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuCores.addAction(self.actionAzul)
        self.menuCores.addAction(self.actionAmarelo)
        self.menuCores.addAction(self.actionVermelho)
        self.menuCores.addAction(self.actionVerde)
        self.menuCores.addSeparator()
        self.menuCores.addAction(self.actionLimpar)
        self.menuSobre.addAction(self.actionNocciolli)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Janela com Menu Personalizado", None))
        self.actionAzul.setText(QCoreApplication.translate("mainWindow", u"Azul", None))
        self.actionAmarelo.setText(QCoreApplication.translate("mainWindow", u"Amarelo", None))
        self.actionVermelho.setText(QCoreApplication.translate("mainWindow", u"Vermelho", None))
        self.actionVerde.setText(QCoreApplication.translate("mainWindow", u"Verde", None))
        self.actionLimpar.setText(QCoreApplication.translate("mainWindow", u"Limpar", None))
        self.actionNocciolli.setText(QCoreApplication.translate("mainWindow", u"M\u00fcller Nocciolli", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Op\u00e7\u00e3o selecionada no menu:", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Preto", None))
        self.menuCores.setTitle(QCoreApplication.translate("mainWindow", u"Cores", None))
        self.menuSobre.setTitle(QCoreApplication.translate("mainWindow", u"Sobre", None))
    # retranslateUi

