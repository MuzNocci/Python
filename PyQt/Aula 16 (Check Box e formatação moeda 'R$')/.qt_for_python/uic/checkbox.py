# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'checkbox.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(336, 356)
        MainWindow.setStyleSheet(u"background-color:rgb(85, 0, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(158, 216, 130, 40))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{background-color:rgb(255, 255, 0);font-weight:bold;font-size:15px;border:0;border-radius:3px;} QPushButton:hover{background-color:rgb(195, 195, 0);}QPushButton:pressed{background-color:rgb(81, 81, 0);}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 146, 120, 30))
        self.label.setStyleSheet(u"font-size:15px;font-weight:bold;color:#fff;")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(50, 80, 91, 17))
        self.checkBox.setStyleSheet(u"color:#fff;font-weight:bold;")
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(50, 120, 91, 17))
        self.checkBox_2.setStyleSheet(u"color:#fff;font-weight:bold;")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(50, 160, 91, 17))
        self.checkBox_3.setStyleSheet(u"color:#fff;font-weight:bold;")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(50, 200, 91, 17))
        self.checkBox_4.setStyleSheet(u"color:#fff;font-weight:bold;")
        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(50, 240, 91, 17))
        self.checkBox_5.setStyleSheet(u"color:#fff;font-weight:bold;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 170, 151, 30))
        self.label_2.setStyleSheet(u"font-size:25px;font-weight:bold;color:rgb(255, 255, 0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora de Pre\u00e7os (Aula 16 - CheckBox)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Valor total:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"R$ 1.500,00", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"R$ 20,00", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"R$ 10,00", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"R$ 32,00", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"R$ 5,50", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
    # retranslateUi

