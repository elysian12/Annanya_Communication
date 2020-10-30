# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_content.ui'
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

class Ui_Maincontent(object):
    def setupUi(self, Maincontent):
        if not Maincontent.objectName():
            Maincontent.setObjectName(u"Maincontent")
        Maincontent.resize(800, 500)
        Maincontent.setMinimumSize(QSize(800, 500))
        self.centralwidget = QWidget(Maincontent)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar_frame = QFrame(self.centralwidget)
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_frame.setMaximumSize(QSize(16777215, 30))
        self.title_bar_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.title_bar_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(13, 0, 0, 0)
        self.title = QLabel(self.title_bar)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(13)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(137, 142, 125);")
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.title)


        self.horizontalLayout.addWidget(self.title_bar)

        self.frame_btns = QFrame(self.title_bar_frame)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setEnabled(True)
        self.frame_btns.setMaximumSize(QSize(120, 16777215))
        self.frame_btns.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_btns)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(14)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(15, 0, 0, 0)
        self.minimise = QPushButton(self.frame_btns)
        self.minimise.setObjectName(u"minimise")
        self.minimise.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:7px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimise.setIcon(icon)

        self.gridLayout.addWidget(self.minimise, 0, 0, 1, 1)

        self.maximize = QPushButton(self.frame_btns)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize.setIcon(icon1)

        self.gridLayout.addWidget(self.maximize, 0, 1, 1, 1)

        self.close = QPushButton(self.frame_btns)
        self.close.setObjectName(u"close")
        self.close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon2)

        self.gridLayout.addWidget(self.close, 0, 2, 1, 1)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        self.main_frame.setFont(font1)
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.main_frame)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 30))
        self.top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 30))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.btn_toggle)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.top_frame = QFrame(self.top_bar)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.top_frame)


        self.verticalLayout_2.addWidget(self.top_bar)

        self.content = QFrame(self.main_frame)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_top_menus)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color :rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_new_entry = QPushButton(self.frame_top_menus)
        self.btn_new_entry.setObjectName(u"btn_new_entry")
        self.btn_new_entry.setMinimumSize(QSize(0, 40))
        self.btn_new_entry.setStyleSheet(u"QPushButton{\n"
"	color :rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_new_entry)

        self.btn_Search = QPushButton(self.frame_top_menus)
        self.btn_Search.setObjectName(u"btn_Search")
        self.btn_Search.setMinimumSize(QSize(0, 40))
        self.btn_Search.setStyleSheet(u"QPushButton{\n"
"	color :rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_Search)


        self.verticalLayout_4.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_7 = QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(40)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label)

        self.pages_widget.addWidget(self.home_page)
        self.search_page = QWidget()
        self.search_page.setObjectName(u"search_page")
        self.verticalLayout_9 = QVBoxLayout(self.search_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.search_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.pages_widget.addWidget(self.search_page)
        self.new_entry_page = QWidget()
        self.new_entry_page.setObjectName(u"new_entry_page")
        self.horizontalLayout_5 = QHBoxLayout(self.new_entry_page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.new_entry_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 28))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.title_2 = QLabel(self.frame_3)
        self.title_2.setObjectName(u"title_2")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(15)
        self.title_2.setFont(font3)
        self.title_2.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.title_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_12.addWidget(self.title_2)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.username = QLineEdit(self.frame_4)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 0))
        self.username.setMaximumSize(QSize(220, 28))
        font4 = QFont()
        font4.setFamily(u"Open Sans Light")
        font4.setPointSize(10)
        self.username.setFont(font4)
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

        self.verticalLayout_10.addWidget(self.username)

        self.username_2 = QLineEdit(self.frame_4)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setMaximumSize(QSize(220, 28))
        self.username_2.setFont(font4)
        self.username_2.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_10.addWidget(self.username_2)

        self.username_3 = QLineEdit(self.frame_4)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setMaximumSize(QSize(220, 28))
        self.username_3.setFont(font4)
        self.username_3.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_10.addWidget(self.username_3)

        self.username_4 = QLineEdit(self.frame_4)
        self.username_4.setObjectName(u"username_4")
        self.username_4.setMaximumSize(QSize(220, 28))
        self.username_4.setFont(font4)
        self.username_4.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_10.addWidget(self.username_4)

        self.username_5 = QLineEdit(self.frame_4)
        self.username_5.setObjectName(u"username_5")
        self.username_5.setMaximumSize(QSize(220, 28))
        self.username_5.setFont(font4)
        self.username_5.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_10.addWidget(self.username_5)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setMaximumSize(QSize(100, 25))
        self.frame_7.setLayoutDirection(Qt.RightToLeft)
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_7)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.new_entry_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(350, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 28))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.username_8 = QLineEdit(self.frame_5)
        self.username_8.setObjectName(u"username_8")
        self.username_8.setMaximumSize(QSize(220, 28))
        self.username_8.setFont(font4)
        self.username_8.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_13.addWidget(self.username_8)

        self.username_7 = QLineEdit(self.frame_5)
        self.username_7.setObjectName(u"username_7")
        self.username_7.setMaximumSize(QSize(220, 28))
        self.username_7.setFont(font4)
        self.username_7.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_13.addWidget(self.username_7)

        self.username_9 = QLineEdit(self.frame_5)
        self.username_9.setObjectName(u"username_9")
        self.username_9.setMaximumSize(QSize(220, 28))
        self.username_9.setFont(font4)
        self.username_9.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_13.addWidget(self.username_9)

        self.username_6 = QLineEdit(self.frame_5)
        self.username_6.setObjectName(u"username_6")
        self.username_6.setMaximumSize(QSize(220, 28))
        self.username_6.setFont(font4)
        self.username_6.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_13.addWidget(self.username_6)

        self.username_10 = QLineEdit(self.frame_5)
        self.username_10.setObjectName(u"username_10")
        self.username_10.setMaximumSize(QSize(220, 28))
        self.username_10.setFont(font4)
        self.username_10.setStyleSheet(u"QLineEdit{\n"
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

        self.verticalLayout_13.addWidget(self.username_10)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMaximumSize(QSize(100, 25))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        self.pushButton.setFont(font5)
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color :rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.pushButton)


        self.verticalLayout_11.addWidget(self.frame_5)


        self.horizontalLayout_5.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.pages_widget.addWidget(self.new_entry_page)

        self.verticalLayout_6.addWidget(self.pages_widget)


        self.horizontalLayout_4.addWidget(self.frame_pages)


        self.verticalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.main_frame)

        Maincontent.setCentralWidget(self.centralwidget)

        self.retranslateUi(Maincontent)

        self.pages_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Maincontent)
    # setupUi

    def retranslateUi(self, Maincontent):
        Maincontent.setWindowTitle(QCoreApplication.translate("Maincontent", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("Maincontent", u"Annanya Communication - Main Window", None))
        self.minimise.setText("")
        self.maximize.setText("")
        self.close.setText("")
        self.btn_toggle.setText("")
        self.btn_home.setText(QCoreApplication.translate("Maincontent", u"HOME", None))
        self.btn_new_entry.setText(QCoreApplication.translate("Maincontent", u"New Entry", None))
        self.btn_Search.setText(QCoreApplication.translate("Maincontent", u"Search", None))
        self.label.setText(QCoreApplication.translate("Maincontent", u"HOME PAGE", None))
        self.label_3.setText(QCoreApplication.translate("Maincontent", u"Search", None))
        self.title_2.setText(QCoreApplication.translate("Maincontent", u"Customer Details", None))
        self.username.setInputMask("")
        self.username.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Account Number", None))
        self.username_2.setInputMask("")
        self.username_2.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Account Name", None))
        self.username_3.setInputMask("")
        self.username_3.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Bank Name", None))
        self.username_4.setInputMask("")
        self.username_4.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Date", None))
        self.username_5.setInputMask("")
        self.username_5.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Amount", None))
        self.username_8.setInputMask("")
        self.username_8.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Via", None))
        self.username_7.setInputMask("")
        self.username_7.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Branch Name", None))
        self.username_9.setInputMask("")
        self.username_9.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Sender Mobile Number", None))
        self.username_6.setInputMask("")
        self.username_6.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Mobile Number", None))
        self.username_10.setInputMask("")
        self.username_10.setPlaceholderText(QCoreApplication.translate("Maincontent", u"Tx-Id", None))
        self.pushButton.setText(QCoreApplication.translate("Maincontent", u"Submit", None))
    # retranslateUi

