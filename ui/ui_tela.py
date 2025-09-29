# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telakmvRRv.ui'
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
    QLabel, QSizePolicy, QWidget)


class Ui_Tela(object):
    def setupUi(self, Tela):
        if not Tela.objectName():
            Tela.setObjectName(u"Tela")
        Tela.resize(696, 510)
        Tela.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.gridLayout = QGridLayout(Tela)
        self.gridLayout.setObjectName(u"gridLayout")
        self.functions = QWidget(Tela)
        self.functions.setObjectName(u"functions")
        self.horizontalLayout = QHBoxLayout(self.functions)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.functions)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.functions)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout.addWidget(self.functions, 1, 0, 1, 1)

        self.widget_2 = QWidget(Tela)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 60))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/radix_logo.jpg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(80, 50))
        self.label_5.setPixmap(QPixmap(u":/newPrefix/vale_logo.png"))
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
        self.label = QLabel(self.titulo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_3.addWidget(self.titulo, 0, 0, 1, 1)


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
        self.label_2.setText(QCoreApplication.translate("Tela", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Tela", u"TextLabel", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("Tela", u"Time Catalogadas/Melhorias", None))
    # retranslateUi

