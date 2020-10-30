# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
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


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(56, 58, 89);\n"
"	color:rgb(220, 220, 220);\n"
"	border-radius:10px;\n"
"}")
        self.drop_shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.drop_shadow_frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 100, 661, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 191);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_descripition = QLabel(self.drop_shadow_frame)
        self.label_descripition.setObjectName(u"label_descripition")
        self.label_descripition.setGeometry(QRect(0, 160, 661, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_descripition.setFont(font1)
        self.label_descripition.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_descripition.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.drop_shadow_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 290, 511, 21))
        self.progressBar.setStyleSheet(u"QProgressBar{	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"QProgressBar:chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.0454545, y1:0.495, x2:1, y2:0.505, stop:0 rgba(254, 121, 191, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.drop_shadow_frame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(10, 320, 661, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.drop_shadow_frame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(0, 350, 661, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.drop_shadow_frame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<strong>Annanya</strong> Communication", None))
        self.label_descripition.setText(QCoreApplication.translate("SplashScreen", u"<strong>Shop</strong> Mangement Software", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>loading...</p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Developed </strong>:Aman Singh   ", None))
    # retranslateUi

