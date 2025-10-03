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
        MainWindow.resize(409, 494)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_pc_2 = QPushButton(self.centralwidget)
        self.btn_pc_2.setObjectName(u"btn_pc_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pc_2.sizePolicy().hasHeightForWidth())
        self.btn_pc_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_pc_2, 0, 0, 1, 2)

        self.btn_palm = QPushButton(self.centralwidget)
        self.btn_palm.setObjectName(u"btn_palm")
        sizePolicy.setHeightForWidth(self.btn_palm.sizePolicy().hasHeightForWidth())
        self.btn_palm.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(32)
        self.btn_palm.setFont(font)

        self.gridLayout.addWidget(self.btn_palm, 6, 1, 1, 1)

        self.btn_pc_1 = QPushButton(self.centralwidget)
        self.btn_pc_1.setObjectName(u"btn_pc_1")
        sizePolicy.setHeightForWidth(self.btn_pc_1.sizePolicy().hasHeightForWidth())
        self.btn_pc_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_pc_1, 0, 2, 1, 1)

        self.btn_on_hand = QPushButton(self.centralwidget)
        self.btn_on_hand.setObjectName(u"btn_on_hand")
        sizePolicy.setHeightForWidth(self.btn_on_hand.sizePolicy().hasHeightForWidth())
        self.btn_on_hand.setSizePolicy(sizePolicy)
        self.btn_on_hand.setFont(font)

        self.gridLayout.addWidget(self.btn_on_hand, 6, 2, 1, 1)

        self.btn_player = QPushButton(self.centralwidget)
        self.btn_player.setObjectName(u"btn_player")
        sizePolicy.setHeightForWidth(self.btn_player.sizePolicy().hasHeightForWidth())
        self.btn_player.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_player, 3, 1, 1, 2)

        self.text = QLabel(self.centralwidget)
        self.text.setObjectName(u"text")
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        self.text.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text, 1, 1, 2, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_palm.setText(QCoreApplication.translate("MainWindow", u"\u270b", None))
        self.btn_on_hand.setText(QCoreApplication.translate("MainWindow", u"\ud83e\udd1a", None))
    # retranslateUi

