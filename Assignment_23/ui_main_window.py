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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.open_file_menu = QAction(MainWindow)
        self.open_file_menu.setObjectName(u"open_file_menu")
        self.new_game_menu = QAction(MainWindow)
        self.new_game_menu.setObjectName(u"new_game_menu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 781, 561))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menunew_game = QMenu(self.menubar)
        self.menunew_game.setObjectName(u"menunew_game")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menunew_game.menuAction())
        self.menunew_game.addAction(self.open_file_menu)
        self.menunew_game.addAction(self.new_game_menu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_file_menu.setText(QCoreApplication.translate("MainWindow", u"open file", None))
        self.new_game_menu.setText(QCoreApplication.translate("MainWindow", u"new game", None))
        self.menunew_game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi
