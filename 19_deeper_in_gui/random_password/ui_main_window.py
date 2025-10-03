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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(431, 360)
        MainWindow.setStyleSheet(u"background-color: rgb(94, 150, 255);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.length_text = QLineEdit(self.centralwidget)
        self.length_text.setObjectName(u"length_text")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length_text.sizePolicy().hasHeightForWidth())
        self.length_text.setSizePolicy(sizePolicy)
        self.length_text.setStyleSheet(u"border: 2px solid Black;\n"
"border-radius: 5px;")
        self.length_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.length_text)

        self.radio_normal = QRadioButton(self.centralwidget)
        self.radio_normal.setObjectName(u"radio_normal")

        self.verticalLayout.addWidget(self.radio_normal)

        self.radio_strong = QRadioButton(self.centralwidget)
        self.radio_strong.setObjectName(u"radio_strong")

        self.verticalLayout.addWidget(self.radio_strong)

        self.radio_very_strong = QRadioButton(self.centralwidget)
        self.radio_very_strong.setObjectName(u"radio_very_strong")

        self.verticalLayout.addWidget(self.radio_very_strong)

        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        self.generate.setStyleSheet(u"border: 2px solid Black;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.generate)

        self.password_output = QLineEdit(self.centralwidget)
        self.password_output.setObjectName(u"password_output")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.password_output.sizePolicy().hasHeightForWidth())
        self.password_output.setSizePolicy(sizePolicy1)
        self.password_output.setStyleSheet(u"border: 2px solid Black;\n"
"border-radius: 10px;")
        self.password_output.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.password_output.setReadOnly(True)

        self.verticalLayout.addWidget(self.password_output)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter lengths of password", None))
        self.radio_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.radio_strong.setText(QCoreApplication.translate("MainWindow", u"Strong", None))
        self.radio_very_strong.setText(QCoreApplication.translate("MainWindow", u"Very strong", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"Generator", None))
        self.password_output.setText("")
    # retranslateUi

