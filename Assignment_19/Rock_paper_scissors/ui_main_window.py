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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(606, 655)
        MainWindow.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_pc = QPushButton(self.centralwidget)
        self.btn_pc.setObjectName(u"btn_pc")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pc.sizePolicy().hasHeightForWidth())
        self.btn_pc.setSizePolicy(sizePolicy)
        self.btn_pc.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: rgb(131, 131, 131);")

        self.gridLayout.addWidget(self.btn_pc, 0, 1, 1, 1)

        self.btn_player = QPushButton(self.centralwidget)
        self.btn_player.setObjectName(u"btn_player")
        sizePolicy.setHeightForWidth(self.btn_player.sizePolicy().hasHeightForWidth())
        self.btn_player.setSizePolicy(sizePolicy)
        self.btn_player.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: rgb(131, 131, 131);")

        self.gridLayout.addWidget(self.btn_player, 2, 1, 1, 1)

        self.btn_stone = QPushButton(self.centralwidget)
        self.btn_stone.setObjectName(u"btn_stone")
        self.btn_stone.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_stone.sizePolicy().hasHeightForWidth())
        self.btn_stone.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(45)
        font.setWeight(QFont.ExtraLight)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QFont.PreferDefault)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.btn_stone.setFont(font)
        self.btn_stone.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: rgb(131, 131, 131);")
        self.btn_stone.setText(u"\ud83c\udfb1")
        self.btn_stone.setIconSize(QSize(180, 180))
        self.btn_stone.setFlat(False)

        self.gridLayout.addWidget(self.btn_stone, 4, 0, 1, 1)

        self.btn_scissors = QPushButton(self.centralwidget)
        self.btn_scissors.setObjectName(u"btn_scissors")
        sizePolicy1.setHeightForWidth(self.btn_scissors.sizePolicy().hasHeightForWidth())
        self.btn_scissors.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(45)
        font1.setKerning(True)
        self.btn_scissors.setFont(font1)
        self.btn_scissors.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: rgb(131, 131, 131);")
        self.btn_scissors.setIconSize(QSize(180, 180))

        self.gridLayout.addWidget(self.btn_scissors, 4, 2, 1, 1)

        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        sizePolicy1.setHeightForWidth(self.btn_paper.sizePolicy().hasHeightForWidth())
        self.btn_paper.setSizePolicy(sizePolicy1)
        self.btn_paper.setFont(font1)
        self.btn_paper.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 25px;\n"
"background-color: rgb(131, 131, 131);")
        self.btn_paper.setIconSize(QSize(180, 180))

        self.gridLayout.addWidget(self.btn_paper, 4, 1, 1, 1)

        self.result_text = QLabel(self.centralwidget)
        self.result_text.setObjectName(u"result_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.result_text.sizePolicy().hasHeightForWidth())
        self.result_text.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        self.result_text.setFont(font2)
        self.result_text.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(131, 131, 131);\n"
"color: rgb(255, 255, 255);")
        self.result_text.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_text, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_pc.setText("")
        self.btn_player.setText("")
        self.btn_scissors.setText(QCoreApplication.translate("MainWindow", u"\u2702", None))
        self.btn_paper.setText(QCoreApplication.translate("MainWindow", u"\ud83d\udcc4", None))
        self.result_text.setText(QCoreApplication.translate("MainWindow", u"Game result: Result", None))
    # retranslateUi

