import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela import Ui_Tela 
from PySide6.QtWidgets import QWidget
from ui.resources_rc import *      
import webbrowser          
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class MainWindow(QWidget, Ui_Tela):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.pushButton.clicked.connect(self.open_pydaq_website)
        self.setWindowTitle("PIMS - Radix/Vale")
        self.pushButton.setIcon(QIcon(":/newPrefix/vale_logo.png"))
        self.pushButton_2.setIcon(QIcon(":/newPrefix/radix_logo.jpg"))
        self.pushButton_2.setIconSize(QSize(150,150))
        self.pushButton.setIconSize(QSize(150,150))

    def open_pydaq_website(self):
        url = "https://samirmartins.github.io/pydaq/"
        webbrowser.open(url)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
