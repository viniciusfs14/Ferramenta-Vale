import sys
from PySide6 import QtWidgets
from ui.ui_main_window import Ui_inicial_Tela  
from ui.resources_rc import *                  

class MainWindow(QtWidgets.QMainWindow, Ui_inicial_Tela):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  
        self.setWindowTitle("Projeto Radix")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())  
