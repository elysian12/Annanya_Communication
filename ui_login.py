# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import file_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(397, 483)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_effect = QFrame(self.centralwidget)
        self.drop_shadow_effect.setObjectName(u"drop_shadow_effect")
        self.drop_shadow_effect.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius:10px;")
        self.drop_shadow_effect.setFrameShape(QFrame.StyledPanel)
        self.drop_shadow_effect.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.drop_shadow_effect)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_bar = QFrame(self.drop_shadow_effect)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"background-color:rgb(30, 30, 30);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(137, 142, 125);")
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_title.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(40, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(20, 0, 16, 16))
        self.btn_close.setMinimumSize(QSize(15, 15))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_minimise = QPushButton(self.frame_btns)
        self.btn_minimise.setObjectName(u"btn_minimise")
        self.btn_minimise.setGeometry(QRect(0, 0, 16, 16))
        self.btn_minimise.setMinimumSize(QSize(15, 15))
        self.btn_minimise.setMaximumSize(QSize(16, 16))
        self.btn_minimise.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"	}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout_2.addWidget(self.title_bar)

        self.frame_2 = QFrame(self.drop_shadow_effect)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.username = QLineEdit(self.frame_2)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(110, 120, 160, 30))
        font2 = QFont()
        font2.setFamily(u"Open Sans Light")
        font2.setPointSize(10)
        self.username.setFont(font2)
        self.username.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(70, 70, 70);\n"
"	border-radius:10px;\n"
"	padding-left:20px;\n"
"	padding-right:20px;\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(150, 150, 150);\n"
"}")
        self.password = QLineEdit(self.frame_2)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(110, 160, 160, 30))
        self.password.setFont(font2)
        self.password.setStyleSheet(u"QLineEdit{\n"
"	border:2px solid rgb(70, 70, 70);\n"
"	border-radius:10px;\n"
"	padding-left:20px;\n"
"	padding-right:20px;\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(85, 170, 255);\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(85, 170, 255);\n"
"	background-color: rgb(150, 150, 150);\n"
"}")
        self.password.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 210, 40, 23))
        self.pushButton.setMaximumSize(QSize(50, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius:8px;\n"
"	background-color: rgb(255, 85, 0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"		\n"
"	background-color: rgba(255, 85, 0, 150);\n"
"}")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 61, 61))
        self.label.setStyleSheet(u"background-image: url(:/newPrefix/profile (1).png);")
        self.label.setPixmap(QPixmap(u":/newPrefix/profile (1).png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.drop_shadow_effect)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("LoginWindow", u"Annanya communication-Login", None))
        self.btn_close.setText("")
        self.btn_minimise.setText("")
        self.username.setInputMask("")
        self.username.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label.setText("")
    # retranslateUi

