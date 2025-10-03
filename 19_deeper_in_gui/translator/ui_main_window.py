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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(416, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(99, 99, 99);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.output_text = QLineEdit(self.centralwidget)
        self.output_text.setObjectName(u"output_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.output_text.sizePolicy().hasHeightForWidth())
        self.output_text.setSizePolicy(sizePolicy1)
        self.output_text.setStyleSheet(u"background-color: rgb(194, 194, 194);\n"
"border: 2px solid white;\n"
"border-radius: 15px;")
        self.output_text.setReadOnly(True)

        self.gridLayout.addWidget(self.output_text, 6, 0, 1, 2)

        self.rdbtn_en_pr = QRadioButton(self.centralwidget)
        self.rdbtn_en_pr.setObjectName(u"rdbtn_en_pr")
        self.rdbtn_en_pr.setStyleSheet(u"background-color: rgb(148, 148, 148);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.rdbtn_en_pr, 2, 0, 1, 1)

        self.rdbtn_pr_en = QRadioButton(self.centralwidget)
        self.rdbtn_pr_en.setObjectName(u"rdbtn_pr_en")
        self.rdbtn_pr_en.setStyleSheet(u"background-color: rgb(148, 148, 148);\n"
"border: 2px solid black;\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.rdbtn_pr_en, 2, 1, 1, 1)

        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        sizePolicy1.setHeightForWidth(self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy1)
        self.input_text.setStyleSheet(u"background-color: rgb(194, 194, 194);\n"
"border: 2px solid white;\n"
"border-radius: 15px;")
        self.input_text.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.input_text, 3, 0, 1, 2)

        self.btn_translate = QPushButton(self.centralwidget)
        self.btn_translate.setObjectName(u"btn_translate")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_translate.sizePolicy().hasHeightForWidth())
        self.btn_translate.setSizePolicy(sizePolicy2)
        self.btn_translate.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"border: 2px solid black;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.btn_translate, 4, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rdbtn_en_pr.setText(QCoreApplication.translate("MainWindow", u"English to Persian", None))
        self.rdbtn_pr_en.setText(QCoreApplication.translate("MainWindow", u"Persian to English", None))
        self.input_text.setText("")
        self.btn_translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
    # retranslateUi

