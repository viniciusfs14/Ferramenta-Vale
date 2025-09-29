import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela import Ui_Tela 
from PySide6.QtWidgets import QWidget
from ui.resources_rc import *                  

class MainWindow(QWidget, Ui_Tela):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
