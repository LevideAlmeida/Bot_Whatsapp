# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import imgs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(270, 340)
        MainWindow.setStyleSheet(u"background: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 40, 87, 60))
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 40pt \"Ubuntu Mono\";\n"
"background-color: rgba(0, 0, 0, 0);\n"
"\n"
"")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(75, 40, 90, 60))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"font: 40pt \"Ubuntu Mono\";\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-10, -10, 281, 361))
        self.label_3.setLineWidth(-1)
        self.label_3.setIndent(-1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 40, 51, 51))
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(60, 140, 155, 70))
        self.startButton.setMinimumSize(QSize(155, 70))
        self.startButton.setMaximumSize(QSize(146, 16777215))
        self.startButton.setStyleSheet(u"background-color: rgb(32, 74, 135);\n"
"color: white;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(60, 235, 155, 70))
        self.exitButton.setMinimumSize(QSize(155, 70))
        self.exitButton.setMaximumSize(QSize(146, 16777215))
        self.exitButton.setStyleSheet(u"background-color: rgb(32, 74, 135);\n"
"color: white;\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.startButton.raise_()
        self.exitButton.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bot whatsapp", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bot", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Zap", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imagens/Images/bg_image.jpg\"/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/imagens/Images/logo_image.png\"/></p></body></html>", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start bot", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

