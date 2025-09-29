
from ui.ui_main_window import Ui_Digitalfilters_NIDAQ_widget
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

class Digital_Filters_NIDAQ_Widget(QMainWindow, Ui_Digitalfilters_NIDAQ_widget):
    def __init__(self, *args):
        super(Ui_Digitalfilters_NIDAQ_widget, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('docs/img/favicon.ico'))
        
        