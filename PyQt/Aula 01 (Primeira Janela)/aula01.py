from PyQt6.QtWidgets import *
import sys
 
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Primeira Janela')
window.setStyleSheet('QWidget{background-color:#333333;}')

window.show()
sys.exit(app.exec())