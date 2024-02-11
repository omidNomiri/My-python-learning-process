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
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.Word_Clock = QWidget()
        self.Word_Clock.setObjectName(u"Word_Clock")
        self.label = QLabel(self.Word_Clock)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 140, 91, 41))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.iran_show_time_lb = QLabel(self.Word_Clock)
        self.iran_show_time_lb.setObjectName(u"iran_show_time_lb")
        self.iran_show_time_lb.setGeometry(QRect(310, 140, 111, 41))
        self.iran_show_time_lb.setFont(font)
        self.iran_show_time_lb.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.Word_Clock)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 200, 101, 41))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.germany_show_time_lb = QLabel(self.Word_Clock)
        self.germany_show_time_lb.setObjectName(u"germany_show_time_lb")
        self.germany_show_time_lb.setGeometry(QRect(310, 200, 111, 41))
        self.germany_show_time_lb.setFont(font)
        self.germany_show_time_lb.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.Word_Clock)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 260, 91, 41))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.usa_show_time_lb = QLabel(self.Word_Clock)
        self.usa_show_time_lb.setObjectName(u"usa_show_time_lb")
        self.usa_show_time_lb.setGeometry(QRect(310, 260, 111, 41))
        self.usa_show_time_lb.setFont(font)
        self.usa_show_time_lb.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.Word_Clock, "")
        self.Alarm = QWidget()
        self.Alarm.setObjectName(u"Alarm")
        self.tabWidget.addTab(self.Alarm, "")
        self.Stop_Watch = QWidget()
        self.Stop_Watch.setObjectName(u"Stop_Watch")
        self.btn_stop = QPushButton(self.Stop_Watch)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setGeometry(QRect(430, 370, 171, 51))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setWeight(QFont.ExtraLight)
        self.btn_stop.setFont(font1)
        self.show_stop_watch_lb = QLabel(self.Stop_Watch)
        self.show_stop_watch_lb.setObjectName(u"show_stop_watch_lb")
        self.show_stop_watch_lb.setGeometry(QRect(260, 120, 261, 81))
        font2 = QFont()
        font2.setPointSize(50)
        self.show_stop_watch_lb.setFont(font2)
        self.show_stop_watch_lb.setAlignment(Qt.AlignCenter)
        self.btn_start = QPushButton(self.Stop_Watch)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setGeometry(QRect(180, 370, 171, 51))
        self.btn_start.setFont(font1)
        self.tabWidget.addTab(self.Stop_Watch, "")
        self.Timer = QWidget()
        self.Timer.setObjectName(u"Timer")
        self.lineEdit = QLineEdit(self.Timer)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(230, 140, 51, 51))
        self.label_2 = QLabel(self.Timer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 140, 16, 41))
        font3 = QFont()
        font3.setPointSize(24)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.Timer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 140, 16, 41))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.Timer)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 140, 51, 51))
        self.lineEdit_3 = QLineEdit(self.Timer)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(390, 140, 51, 51))
        self.tabWidget.addTab(self.Timer, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clock", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"iran", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"germany", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"usa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Word_Clock), QCoreApplication.translate("MainWindow", u"Word Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Alarm), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.show_stop_watch_lb.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Stop_Watch), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Timer), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

