from PyQt6.QtWidgets import *
import sys
 
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Segunda Janela')
window.resize(300,100)
window.setStyleSheet('QWidget{background-color:#0000ff;}')

label = QLabel(window)
label.setText('Adicionando Label e inserindo Texto.')
label.setStyleSheet('QLabel{color:#FFFFFF;font-weight:bold;}')
label.move(50,40)

window.show()
sys.exit(app.exec())