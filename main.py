import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela import Ui_Tela 
from PySide6.QtWidgets import QWidget
from ui.resources_rc import *      
import webbrowser          
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from chamados import ChamadosWindow
import subprocess

class MainWindow(QWidget, Ui_Tela):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.setWindowTitle("PIMS - Radix/Vale")
        self.showMaximized()    
        self.chamados_window = None

        # Personalização dos botões
        self.pushButton.setIcon(QIcon(":/newPrefix/fila_logo.png"))
        self.pushButton_2.setIcon(QIcon(":/newPrefix/controle_logo.png"))
        self.pushButton_3.setIcon(QIcon(":/newPrefix/acessos_logo.png"))
        self.pushButton_4.setIcon(QIcon(":/newPrefix/chamados_logo.png"))
        self.site_button.setIcon(QIcon(":/newPrefix/pimslogo.png"))
    

        # Tamanho dos botões
        self.site_button.setIconSize(QSize(250,250))
        self.pushButton_3.setIconSize(QSize(150,150))
        self.pushButton_4.setIconSize(QSize(150,150))
        self.pushButton_2.setIconSize(QSize(150,150))
        self.pushButton.setIconSize(QSize(150,150))

        # Conexão dos botões com as funções
        self.site_button.clicked.connect(self.open_site)
        self.pushButton_2.clicked.connect(self.open_planilha)
        self.pushButton.clicked.connect(self.open_fila)
        self.pushButton_4.clicked.connect(self.open_chamados)


    def open_fila(self):
        url = "https://vale.service-now.com/now/nav/ui/classic/params/target/%24vtb.do%3Fsysparm_board%3D8c50d5d4fbf342505019f3636eefdc7a"
        webbrowser.open(url)
        
    def open_planilha(self):
        controle = r"Controle Suporte VALE - Catalogadas - Oficial (testes).xlsm"
        subprocess.Popen(["start", "excel", controle], shell=True)

    def open_site(self):
        url = "https://globalvale.sharepoint.com/teams/PIMS"
        webbrowser.open(url)

    def open_acessos(self):
        acesso = "https://radixengazure.sharepoint.com/:w:/r/sites/VALE-FMDS-PIMSCatalogadasMelhorias/Documentos%20Compartilhados/PIMS/01%20-%20Documentos%20de%20Apoio/VALE%20%E2%80%93%20REdiscover%20PIMS%20-%20Acessos.docx?d=wbc5e1361b13047189129c8dece18f2d9&csf=1&web=1&e=JjMAbX"
        subprocess.Popen(["start", "winword", acesso], shell=True)

    def open_chamados(self):
        if self.chamados_window is None:
            self.chamados_window = ChamadosWindow()
        self.chamados_window.show()
        self.chamados_window.raise_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ui\\logoapp.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
