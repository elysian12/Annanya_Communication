import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, Qt,
                            QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPixmap, QPainter, QRadialGradient)
from PySide2.QtWidgets import *
# ==> Splash Screen
from splash_screen import Ui_SplashScreen

# ==> Login Screen
from ui_login import Ui_LoginWindow

# ==> Main content
from ui_main_content import Ui_Maincontent

# ==> import function file
from ui_function import *

# ==>Globals
counter = 0

# main content window
class Maincontent(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Maincontent()
        self.ui.setupUi(self)

        def movewindow(event):
            #if left click move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # set title bar
        self.ui.title_bar_frame.mouseMoveEvent = movewindow   

        # toggle button 
        self.ui.btn_toggle.clicked.connect(lambda : UIContentFunction.toggleMenu(self,200,True))

        # Home Page
        self.ui.btn_home.clicked.connect(lambda : self.ui.pages_widget.setCurrentWidget(self.ui.home_page))         
        # New Entry
        self.ui.btn_new_entry.clicked.connect(lambda : self.ui.pages_widget.setCurrentWidget(self.ui.new_entry_page))

        # Search
        self.ui.btn_Search.clicked.connect(lambda : self.ui.pages_widget.setCurrentWidget(self.ui.search_page))

        #app functions
        UIContentFunction.uidefinition(self)
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()     

# login window
class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        #move Window
        def movewindow(event):
            #if left click move window
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # set title bar
        self.ui.title_bar.mouseMoveEvent = movewindow             
    
        #app function
        UIFunction.uidefinition(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()        
    #validity check 
    def check(self):
        if self.ui.username.text() == "amanasr" and self.ui.password.text() == "9119831111":
            self.main = Maincontent()
            self.main.show()
            self.close()
        elif self.ui.username.text() == "" or self.ui.password.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Annanya Communication Error")
            msg.setText("Username or Password is Empty")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry|QMessageBox.Close) 
            x = msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Annanya Communication Error")
            msg.setText("Username or Password is incorrect")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Retry|QMessageBox.Close) 
            x = msg.exec_()   


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI==> Interface Code
        ##########################################################

        # remove titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop_shadow_Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)
        
        # Qtimer==>start
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # timer in millisecond
        self.timer.start(35)

        ##initate text
        self.ui.label_descripition.setText("<strong>Welcome</strong>")
        QtCore.QTimer.singleShot(1500,lambda: self.ui.label_descripition.setText("<strong>Loading</strong> Database"))
        QtCore.QTimer.singleShot(3000,lambda: self.ui.label_descripition.setText("<strong>Loading</strong> User Interface"))
        # show ==> main window
        self.show()

    # ==> APP Function
    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        # stop splash Screen
        if counter > 100:
            self.timer.stop()

            #show login window
            self.main = LoginWindow()
            self.main.show()

            #close splash screen
            self.close()

        # increaseing timer 
        counter += 1             


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
