import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela import Ui_Tela 
from PySide6.QtWidgets import QWidget
from ui.resources_rc import *      
import webbrowser          
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import subprocess

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
        self.pushButton_2.clicked.connect(self.open_planilha)

    def open_pydaq_website(self):
        url = "https://vale.service-now.com/now/nav/ui/classic/params/target/%24vtb.do%3Fsysparm_board%3D8c50d5d4fbf342505019f3636eefdc7a"
        webbrowser.open(url)
        
    def open_planilha(self):
        controle = r"Controle Suporte VALE - Catalogadas - Oficial.xlsm"
        subprocess.Popen(["start", "excel", controle], shell=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
