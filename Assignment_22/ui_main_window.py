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
    QSizePolicy, QTextEdit, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_TODOAPP(object):
    def setupUi(self, TODOAPP):
        if not TODOAPP.objectName():
            TODOAPP.setObjectName(u"TODOAPP")
        TODOAPP.resize(828, 597)
        self.centralwidget = QWidget(TODOAPP)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setGeometry(QRect(9, 59, 531, 531))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setStyleSheet(u"background-color: rgb(0, 255, 255);border-radius: 15px;")
        self.grid_Layout = QGridLayout(self.gridWidget)
        self.grid_Layout.setObjectName(u"grid_Layout")
        self.grid_Layout.setHorizontalSpacing(5)
        self.grid_Layout.setVerticalSpacing(10)
        self.grid_Layout.setContentsMargins(25, 25, 25, 25)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 10, 231, 41))
        font = QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.verticalWidget = QWidget(self.centralwidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(550, 60, 274, 531))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy1)
        self.verticalWidget.setStyleSheet(u"background-color: rgb(255, 149, 0);border-radius: 15px;")
        self.gridLayout = QGridLayout(self.verticalWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.title_text = QLineEdit(self.verticalWidget)
        self.title_text.setObjectName(u"title_text")
        sizePolicy1.setHeightForWidth(self.title_text.sizePolicy().hasHeightForWidth())
        self.title_text.setSizePolicy(sizePolicy1)
        self.title_text.setStyleSheet(u"background-color: rgb(147, 147, 147);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.title_text, 2, 0, 1, 1)

        self.label_5 = QLabel(self.verticalWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.verticalWidget1 = QWidget(self.verticalWidget)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        sizePolicy2.setHeightForWidth(self.verticalWidget1.sizePolicy().hasHeightForWidth())
        self.verticalWidget1.setSizePolicy(sizePolicy2)
        self.verticalWidget1.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"border-radius: 10px; ")
        self.verticalLayout = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.verticalWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.rd_imp_qui = QRadioButton(self.verticalWidget1)
        self.rd_imp_qui.setObjectName(u"rd_imp_qui")

        self.verticalLayout.addWidget(self.rd_imp_qui)

        self.rd_imp_not_qui = QRadioButton(self.verticalWidget1)
        self.rd_imp_not_qui.setObjectName(u"rd_imp_not_qui")

        self.verticalLayout.addWidget(self.rd_imp_not_qui)

        self.rd_not_imp_qui = QRadioButton(self.verticalWidget1)
        self.rd_not_imp_qui.setObjectName(u"rd_not_imp_qui")

        self.verticalLayout.addWidget(self.rd_not_imp_qui)

        self.rd_not_imp_not_qui = QRadioButton(self.verticalWidget1)
        self.rd_not_imp_not_qui.setObjectName(u"rd_not_imp_not_qui")

        self.verticalLayout.addWidget(self.rd_not_imp_not_qui)


        self.gridLayout.addWidget(self.verticalWidget1, 5, 0, 1, 1)

        self.dec_text_box = QTextEdit(self.verticalWidget)
        self.dec_text_box.setObjectName(u"dec_text_box")
        sizePolicy1.setHeightForWidth(self.dec_text_box.sizePolicy().hasHeightForWidth())
        self.dec_text_box.setSizePolicy(sizePolicy1)
        self.dec_text_box.setStyleSheet(u"background-color: rgb(147, 147, 147);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.dec_text_box, 4, 0, 1, 2)

        self.dateEdit = QDateEdit(self.verticalWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy2.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.dateEdit, 7, 0, 1, 2)

        self.timeEdit = QTimeEdit(self.verticalWidget)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy2.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.timeEdit, 9, 0, 1, 2)

        self.btn_add_task = QPushButton(self.verticalWidget)
        self.btn_add_task.setObjectName(u"btn_add_task")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_add_task.sizePolicy().hasHeightForWidth())
        self.btn_add_task.setSizePolicy(sizePolicy3)
        self.btn_add_task.setStyleSheet(u"background-color: rgb(6, 203, 29);\n"
"color: rgb(0, 0, 255);")

        self.gridLayout.addWidget(self.btn_add_task, 2, 1, 2, 1)

        TODOAPP.setCentralWidget(self.centralwidget)

        self.retranslateUi(TODOAPP)

        QMetaObject.connectSlotsByName(TODOAPP)
    # setupUi

    def retranslateUi(self, TODOAPP):
        TODOAPP.setWindowTitle(QCoreApplication.translate("TODOAPP", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("TODOAPP", u"Todo App", None))
        self.label.setText(QCoreApplication.translate("TODOAPP", u"title", None))
        self.label_5.setText(QCoreApplication.translate("TODOAPP", u"time", None))
        self.label_2.setText(QCoreApplication.translate("TODOAPP", u"description", None))
        self.label_4.setText(QCoreApplication.translate("TODOAPP", u"date", None))
        self.label_3.setText(QCoreApplication.translate("TODOAPP", u"priority", None))
        self.rd_imp_qui.setText(QCoreApplication.translate("TODOAPP", u"important And quick", None))
        self.rd_imp_not_qui.setText(QCoreApplication.translate("TODOAPP", u"important Not quick", None))
        self.rd_not_imp_qui.setText(QCoreApplication.translate("TODOAPP", u"Not important But quick", None))
        self.rd_not_imp_not_qui.setText(QCoreApplication.translate("TODOAPP", u"Not important Not quick", None))
        self.btn_add_task.setText(QCoreApplication.translate("TODOAPP", u"add task", None))
    # retranslateUi

