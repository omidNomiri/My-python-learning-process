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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QTimeEdit, QWidget)

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
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 140, 51, 20))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.rd_imp_qui = QRadioButton(self.centralwidget)
        self.rd_imp_qui.setObjectName(u"rd_imp_qui")
        self.rd_imp_qui.setGeometry(QRect(660, 170, 141, 21))
        self.rd_imp_not_qui = QRadioButton(self.centralwidget)
        self.rd_imp_not_qui.setObjectName(u"rd_imp_not_qui")
        self.rd_imp_not_qui.setGeometry(QRect(660, 210, 141, 21))
        self.rd_not_imp_qui = QRadioButton(self.centralwidget)
        self.rd_not_imp_qui.setObjectName(u"rd_not_imp_qui")
        self.rd_not_imp_qui.setGeometry(QRect(660, 190, 161, 21))
        self.rd_not_imp_not_qui = QRadioButton(self.centralwidget)
        self.rd_not_imp_not_qui.setObjectName(u"rd_not_imp_not_qui")
        self.rd_not_imp_not_qui.setGeometry(QRect(660, 230, 161, 21))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(660, 270, 110, 22))
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(660, 320, 118, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(660, 250, 31, 20))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 300, 31, 20))
        self.label_5.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add_task.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"description", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"priority", None))
        self.rd_imp_qui.setText(QCoreApplication.translate("MainWindow", u"important And quick", None))
        self.rd_imp_not_qui.setText(QCoreApplication.translate("MainWindow", u"important Not quick", None))
        self.rd_not_imp_qui.setText(QCoreApplication.translate("MainWindow", u"Not important But quick", None))
        self.rd_not_imp_not_qui.setText(QCoreApplication.translate("MainWindow", u"Not important Not quick", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"time", None))
    # retranslateUi

