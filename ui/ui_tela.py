# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telaXryQUz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)


class Ui_Tela(object):
    def setupUi(self, Tela):
        if not Tela.objectName():
            Tela.setObjectName(u"Tela")
        Tela.resize(800, 510)
        Tela.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.gridLayout = QGridLayout(Tela)
        self.gridLayout.setObjectName(u"gridLayout")
        self.functions = QWidget(Tela)
        self.functions.setObjectName(u"functions")
        self.horizontalLayout = QHBoxLayout(self.functions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.functions)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_3)

        self.line_2 = QFrame(self.functions)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.widget_4 = QWidget(self.functions)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_5 = QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_4)

        self.line_3 = QFrame(self.functions)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.widget_5 = QWidget(self.functions)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_6 = QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_6.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_5)

        self.line_5 = QFrame(self.functions)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.widget_6 = QWidget(self.functions)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_7 = QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_4 = QPushButton(self.widget_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_7.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_6)


        self.gridLayout.addWidget(self.functions, 1, 0, 1, 1)

        self.widget_2 = QWidget(Tela)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.widget_2.setStyleSheet(u"background-color: #00565F;\n"
"color: white;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(80, 150))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/radixlogonew.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(80, 50))
        self.label_5.setPixmap(QPixmap(u":/newPrefix/valenew.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.gridLayout.addWidget(self.widget_2, 3, 0, 1, 1)

        self.widget = QWidget(Tela)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.titulo = QWidget(self.widget)
        self.titulo.setObjectName(u"titulo")
        self.gridLayout_2 = QGridLayout(self.titulo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.site_button = QPushButton(self.titulo)
        self.site_button.setObjectName(u"site_button")

        self.gridLayout_2.addWidget(self.site_button, 0, 0, 1, 1)

        self.label_7 = QLabel(self.titulo)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_3.addWidget(self.titulo, 0, 0, 1, 1)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.line = QFrame(Tela)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)


        self.retranslateUi(Tela)

        QMetaObject.connectSlotsByName(Tela)
    # setupUi

    def retranslateUi(self, Tela):
        Tela.setWindowTitle(QCoreApplication.translate("Tela", u"Form", None))
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Tela", u"Fila Catalogadas", None))
        self.pushButton_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Tela", u"Planilha de Controle", None))
        self.label_6.setText(QCoreApplication.translate("Tela", u"Acessos", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_8.setText(QCoreApplication.translate("Tela", u"Chamados", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.site_button.setText("")
        self.label_7.setText(QCoreApplication.translate("Tela", u"Central de Apoio - PIMS", None))
    # retranslateUi

