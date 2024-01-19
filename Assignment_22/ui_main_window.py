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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1013, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_add_task = QPushButton(self.centralwidget)
        self.btn_add_task.setObjectName(u"btn_add_task")
        self.btn_add_task.setGeometry(QRect(910, 40, 91, 31))
        self.dec_text_box = QTextEdit(self.centralwidget)
        self.dec_text_box.setObjectName(u"dec_text_box")
        self.dec_text_box.setGeometry(QRect(660, 80, 241, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(660, 10, 41, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(660, 60, 71, 20))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.title_text = QLineEdit(self.centralwidget)
        self.title_text.setObjectName(u"title_text")
        self.title_text.setGeometry(QRect(660, 30, 241, 21))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 641, 581))
        self.grid_Layout = QGridLayout(self.gridLayoutWidget)
        self.grid_Layout.setObjectName(u"grid_Layout")
        self.grid_Layout.setHorizontalSpacing(5)
        self.grid_Layout.setVerticalSpacing(10)
        self.grid_Layout.setContentsMargins(25, 25, 25, 25)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add_task.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"description", None))
    # retranslateUi

