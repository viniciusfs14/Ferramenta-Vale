from ui.ui_tela2 import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import sys

class ChamadosWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Chamados - PIMS")
        self.setWindowIcon(QIcon(":/newPrefix/chamados_logo.png"))

        # Personalização dos botões
        self.criar_tags.setIcon(QIcon(":/newPrefix/newtags.png"))
        self.telavit.setIcon(QIcon(":/newPrefix/telavitorialogo.png"))
        self.telasul.setIcon(QIcon(":/newPrefix/telasulsudestelogo.png"))
        self.criar_tags.setIconSize(QSize(250,250))
        self.telavit.setIconSize(QSize(250,250))
        self.telasul.setIconSize(QSize(250,250))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ui\\logoapp.png"))
    window = ChamadosWindow()
    window.show()
    sys.exit(app.exec())