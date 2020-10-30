# Gui application
from main import *

# ===> Global

Global_state = 0


class UIFunction(LoginWindow):

    # UI Definition
    def uidefinition(self):
        # remove titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # minimize
        self.ui.btn_minimise.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_minimise.setToolTip("Minimise")

        # close
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_close.setToolTip("Close")

        # login check
        self.ui.pushButton.clicked.connect(lambda: self.check())


class UIContentFunction(Maincontent):
    # UI Definition
    def uidefinition(self):
        # remove titlebar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # maxmize
        self.ui.maximize.clicked.connect(
            lambda: UIContentFunction.maxmize_restore(self))

        # minimize
        self.ui.minimise.clicked.connect(lambda: self.showMinimized())
        self.ui.minimise.setToolTip("Minimise")

        # close
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.close.setToolTip("Close")

    def toggleMenu(self, maxwidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            maxExtend = maxwidth
            standard = 70

            if width == 70:
                widthExtended = maxwidth
            else:
                widthExtended = standard
            # Animation
            self.animation = QPropertyAnimation(
                self.ui.frame_left_menu, b"minimumW idth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

    def maxmize_restore(self):
        global Global_state
        status = Global_state

        # If not maximized
        if status == 0:
            self.showMaximized

            # ==> set global state = 1
            Global_state = 1
            self.ui.main_frame.setContentsMargins(0, 0, 0, 0)
            self.ui.main_frame.setStyleSheet(
                "background-color: rgb(45, 45, 45);")
            self.ui.maximize.setToolTip("Restore")
        else:
            Global_state = 0
            self.resize(self.width()+1, self.height()+1)
            self.ui.main_frame.setContentsMargins(10, 10, 10, 10)
            self.ui.main_frame.setStyleSheet(
                "background-color: rgb(45, 45, 45);")
            self.ui.maximize.setToolTip("Maxmize")
