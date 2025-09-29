# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowVRDMug.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QToolBar, QWidget)
from ui.resources_rc import *  

class Ui_inicial_Tela(object):
    def setupUi(self, inicial_Tela):
        if not inicial_Tela.objectName():
            inicial_Tela.setObjectName(u"inicial_Tela")
        inicial_Tela.resize(801, 552)
        inicial_Tela.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.actionAbout = QAction(inicial_Tela)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(inicial_Tela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.logos = QWidget(self.centralwidget)
        self.logos.setObjectName(u"logos")
        self.logos.setMinimumSize(QSize(0, 50))
        self.logos.setMaximumSize(QSize(16777215, 50))
        self.gridLayout = QGridLayout(self.logos)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.logos)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 50))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/vale_logo.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.logos)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 100))
        self.label.setPixmap(QPixmap(u":/newPrefix/radix_logo.jpg"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.logos, 2, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(44)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_4.addWidget(self.widget_3, 2, 0, 1, 1)

        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        inicial_Tela.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(inicial_Tela)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 33))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        inicial_Tela.setMenuBar(self.menubar)
        self.toolBar = QToolBar(inicial_Tela)
        self.toolBar.setObjectName(u"toolBar")
        inicial_Tela.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionAbout)

        self.retranslateUi(inicial_Tela)

        QMetaObject.connectSlotsByName(inicial_Tela)
    # setupUi

    def retranslateUi(self, inicial_Tela):
        inicial_Tela.setWindowTitle(QCoreApplication.translate("inicial_Tela", u"MainWindow", None))
        self.actionAbout.setText(QCoreApplication.translate("inicial_Tela", u"About", None))
        self.label_2.setText("")
        self.label.setText("")
        self.label_5.setText(QCoreApplication.translate("inicial_Tela", u"Time Catalogadas/Melhorias", None))
        self.label_3.setText(QCoreApplication.translate("inicial_Tela", u"\u2328\ufe0f", None))
        self.label_4.setText(QCoreApplication.translate("inicial_Tela", u"\ud83d\udcbb", None))
        self.menuMenu.setTitle(QCoreApplication.translate("inicial_Tela", u"Menu", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("inicial_Tela", u"toolBar", None))
    # retranslateUi

