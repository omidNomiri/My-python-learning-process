# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(409, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_player = QPushButton(self.centralwidget)
        self.btn_player.setObjectName(u"btn_player")
        self.btn_player.setGeometry(QRect(130, 260, 150, 200))
        self.btn_pc_1 = QPushButton(self.centralwidget)
        self.btn_pc_1.setObjectName(u"btn_pc_1")
        self.btn_pc_1.setGeometry(QRect(240, 20, 150, 200))
        self.btn_pc_2 = QPushButton(self.centralwidget)
        self.btn_pc_2.setObjectName(u"btn_pc_2")
        self.btn_pc_2.setGeometry(QRect(20, 20, 150, 200))
        self.text = QLabel(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(150, 230, 100, 25))
        self.text.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

