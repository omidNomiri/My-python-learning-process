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
    QMenuBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.open_file_menu = QAction(MainWindow)
        self.open_file_menu.setObjectName(u"open_file_menu")
        self.new_game_menu = QAction(MainWindow)
        self.new_game_menu.setObjectName(u"new_game_menu")
        self.solve_menu = QAction(MainWindow)
        self.solve_menu.setObjectName(u"solve_menu")
        self.about_menu = QAction(MainWindow)
        self.about_menu.setObjectName(u"about_menu")
        self.help_menu = QAction(MainWindow)
        self.help_menu.setObjectName(u"help_menu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 781, 541))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.dark_mode_toggle_btn = QPushButton(self.centralwidget)
        self.dark_mode_toggle_btn.setObjectName(u"dark_mode_toggle_btn")
        self.dark_mode_toggle_btn.setGeometry(QRect(760, 0, 31, 31))
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(720, 0, 31, 31))
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
        self.menunew_game.addAction(self.solve_menu)
        self.menunew_game.addAction(self.about_menu)
        self.menunew_game.addAction(self.help_menu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_file_menu.setText(QCoreApplication.translate("MainWindow", u"open file", None))
        self.new_game_menu.setText(QCoreApplication.translate("MainWindow", u"new game", None))
        self.solve_menu.setText(QCoreApplication.translate("MainWindow", u"solve", None))
        self.about_menu.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.help_menu.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.menunew_game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi

