from PyQt5 import QtCore, QtGui, QtWidgets
import random
import time
import sys

#clasa p-tru fereastra de start
class Ui_StartWindow(object):

    #style Start Window
    def setupUi(self, StartWindow):

        #stiluri p-tru fereastra principala
        StartWindow.setObjectName("StartWindow")
        StartWindow.setEnabled(True)
        StartWindow.resize(800, 600)
        StartWindow.setStyleSheet("background-color: rgb(247, 247, 247);")
        StartWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)

        #widget
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")

        #aria butoanelor
        self.frameStart = QtWidgets.QFrame(self.centralwidget)
        self.frameStart.setGeometry(QtCore.QRect(0, 450, 801, 80))
        self.frameStart.setAutoFillBackground(False)
        self.frameStart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameStart.setObjectName("frameStart")

        #fontul (la btn)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        #butonul start
        self.start = QtWidgets.QPushButton(self.frameStart)
        self.start.setGeometry(QtCore.QRect(170, 20, 131, 41))
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setStyleSheet("background-color: rgb(130, 0, 124);\n"
"color: rgb(255, 255, 255);")
        self.start.setObjectName("start")

        #butonul settings
        self.settings = QtWidgets.QPushButton(self.frameStart)
        self.settings.setGeometry(QtCore.QRect(340, 20, 131, 41))
        self.settings.setFont(font)
        self.settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings.setStyleSheet("background-color: rgb(130, 0, 124);\n"
"color: rgb(255, 255, 255);")
        self.settings.setObjectName("settings")

        #butonul exit
        self.exit = QtWidgets.QPushButton(self.frameStart)
        self.exit.setGeometry(QtCore.QRect(510, 20, 131, 41))
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("background-color: rgb(130, 0, 124);\n"
"color: rgb(255, 255, 255);")
        self.exit.setObjectName("exit")

        #font style pentru headStartText
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        #headStartText (Header)
        self.headStartText = QtWidgets.QLabel(self.centralwidget)
        self.headStartText.setGeometry(QtCore.QRect(0, 20, 801, 51))
        self.headStartText.setFont(font)
        self.headStartText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headStartText.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"font: 75 36pt \"Segoe Print\";")
        self.headStartText.setAlignment(QtCore.Qt.AlignCenter)
        self.headStartText.setObjectName("headStartText")

        #style img
        self.imgStart = QtWidgets.QLabel(self.centralwidget)
        self.imgStart.setGeometry(QtCore.QRect(-30, 100, 521, 331))
        self.imgStart.setText("")
        self.imgStart.setPixmap(QtGui.QPixmap("magic-8.png"))
        self.imgStart.setScaledContents(True)
        self.imgStart.setObjectName("imgStart")


        #font modificat pentru titleStart
        font.setBold(True)
        font.setWeight(75)

        #style titleStart
        self.titleStart = QtWidgets.QLabel(self.centralwidget)
        self.titleStart.setGeometry(QtCore.QRect(420, 100, 321, 331))
        self.titleStart.setFont(font)
        self.titleStart.setAlignment(QtCore.Qt.AlignCenter)
        self.titleStart.setWordWrap(True)
        self.titleStart.setObjectName("titleStart")
        StartWindow.setCentralWidget(self.centralwidget)

        #style menubar
        self.menubar = QtWidgets.QMenuBar(StartWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        StartWindow.setMenuBar(self.menubar)
        #style statusbar
        self.statusbar = QtWidgets.QStatusBar(StartWindow)
        self.statusbar.setObjectName("statusbar")

        StartWindow.setStatusBar(self.statusbar)
        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    #retranslarea UI
    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Magic 8 Ball"))
        StartWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.start.setText(_translate("StartWindow", "START"))
        self.settings.setText(_translate("StartWindow", "SETTINGS"))
        self.exit.setText(_translate("StartWindow", "EXIT"))
        self.headStartText.setText(_translate("StartWindow", "Welcome"))
        self.titleStart.setText(_translate("StartWindow", "The Magic 8 Ball"))


#clasa p-tru fereastra de setari
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #style fereastra setarilor
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(247, 247, 247);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #frame pentru btn
        self.frameSettings = QtWidgets.QFrame(self.centralwidget)
        self.frameSettings.setGeometry(QtCore.QRect(0, 450, 801, 80))
        self.frameSettings.setAutoFillBackground(False)
        self.frameSettings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSettings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSettings.setObjectName("frameSettings")

        # font style
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        #butonul start
        self.start = QtWidgets.QPushButton(self.frameSettings)
        self.start.setGeometry(QtCore.QRect(300, 20, 191, 41))
        self.start.setFont(font)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setStyleSheet("background-color: rgb(130, 0, 124);\n"
"color: rgb(255, 255, 255);")
        self.start.setObjectName("start")

        #font style
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setItalic(False)
        font.setWeight(9)

        #head text
        self.headSettingsText = QtWidgets.QLabel(self.centralwidget)
        self.headSettingsText.setGeometry(QtCore.QRect(0, 20, 801, 41))
        self.headSettingsText.setFont(font)
        self.headSettingsText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headSettingsText.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"font: 75 30pt \"Segoe Print\";")
        self.headSettingsText.setAlignment(QtCore.Qt.AlignCenter)
        self.headSettingsText.setObjectName("headSettingsText")

        #img settings
        self.imgSettings = QtWidgets.QLabel(self.centralwidget)
        self.imgSettings.setGeometry(QtCore.QRect(-30, 100, 521, 331))
        self.imgSettings.setText("")
        self.imgSettings.setPixmap(QtGui.QPixmap("magic-8.png"))
        self.imgSettings.setScaledContents(True)
        self.imgSettings.setObjectName("imgSettings")

        #font style
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        #style titleSettings
        self.titleSettings = QtWidgets.QLabel(self.centralwidget)
        self.titleSettings.setGeometry(QtCore.QRect(420, 100, 321, 91))
        self.titleSettings.setFont(font)
        self.titleSettings.setAlignment(QtCore.Qt.AlignCenter)
        self.titleSettings.setWordWrap(True)
        self.titleSettings.setObjectName("titleSettings")

        #frame p-tru resolution
        self.frame_2Settings = QtWidgets.QFrame(self.centralwidget)
        self.frame_2Settings.setGeometry(QtCore.QRect(420, 230, 331, 181))
        self.frame_2Settings.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2Settings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2Settings.setObjectName("frame_2Settings")

        #font style
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.labelSettings = QtWidgets.QLabel(self.frame_2Settings)
        self.labelSettings.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.labelSettings.setFont(font)
        self.labelSettings.setObjectName("labelSettings")
        self.radioButtonSett = QtWidgets.QRadioButton(self.frame_2Settings)

        #style font radio
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        #3 radio btn
        self.radioButtonSett.setGeometry(QtCore.QRect(20, 70, 311, 17))
        self.radioButtonSett.setFont(font)
        self.radioButtonSett.setObjectName("radioButtonSett")

        self.radioButton_2Sett = QtWidgets.QRadioButton(self.frame_2Settings)
        self.radioButton_2Sett.setGeometry(QtCore.QRect(20, 110, 311, 17))
        self.radioButton_2Sett.setFont(font)
        self.radioButton_2Sett.setObjectName("radioButton_2Sett")

        self.radioButton_3Sett = QtWidgets.QRadioButton(self.frame_2Settings)
        self.radioButton_3Sett.setGeometry(QtCore.QRect(20, 150, 311, 17))
        self.radioButton_3Sett.setFont(font)
        self.radioButton_3Sett.setObjectName("radioButton_3Sett")


        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # retranslarea UI
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Magic 8 Ball"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.start.setText(_translate("MainWindow", "START"))
        self.headSettingsText.setText(_translate("MainWindow", "Setings"))
        self.titleSettings.setText(_translate("MainWindow", "The Magic 8 Ball"))
        self.labelSettings.setText(_translate("MainWindow", "* Resolution"))
        self.radioButtonSett.setText(_translate("MainWindow", "1000x800"))
        self.radioButton_2Sett.setText(_translate("MainWindow", "800x600"))
        self.radioButton_3Sett.setText(_translate("MainWindow", "620x400"))

#clasa p-tru fereastra cea mai mare
class Ui_LargeWindow(object):

    #setup UI
    def setupUi(self, LargeWindow):

        #general style window LARGE
        LargeWindow.setObjectName("LargeWindow")
        LargeWindow.setEnabled(True)
        LargeWindow.resize(1000, 800)
        LargeWindow.setStyleSheet("background-color: rgb(130, 0, 124);")
        LargeWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)

        #centare
        self.centralwidget = QtWidgets.QWidget(LargeWindow)
        self.centralwidget.setObjectName("centralwidget")

        #style frame (input si btn)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 660, 981, 61))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        #input
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 571, 51))
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        #font style pushButton
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)

        #ask btn
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(670, 10, 181, 51))
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        # font style pushButton
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        #style head text
        self.headText = QtWidgets.QLabel(self.centralwidget)
        self.headText.setGeometry(QtCore.QRect(0, 30, 991, 71))
        self.headText.setFont(font)
        self.headText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headText.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"font: 75 36pt \"Segoe Print\";")
        self.headText.setAlignment(QtCore.Qt.AlignCenter)
        self.headText.setObjectName("headText")

        #style raspuns label
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(10, 570, 981, 61))
        self.answer.setStyleSheet("font: 63 18pt \"Open Sans\";\n"
"color: rgb(255, 255, 255);")
        self.answer.setScaledContents(False)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")

        #style img
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(200, 130, 601, 401))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("ball.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")

        LargeWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(LargeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")

        LargeWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(LargeWindow)
        self.statusbar.setObjectName("statusbar")
        LargeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LargeWindow)
        QtCore.QMetaObject.connectSlotsByName(LargeWindow)

    # retranslarea UI
    def retranslateUi(self, LargeWindow):
        _translate = QtCore.QCoreApplication.translate
        LargeWindow.setWindowTitle(_translate("LargeWindow", "Magic 8 Ball"))
        LargeWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pushButton.setText(_translate("LargeWindow", "Ask"))
        self.headText.setText(_translate("LargeWindow", "The Magic 8 Ball"))
        self.answer.setText(_translate("LargeWindow", "Ai o intrebare?"))

#clasa p-tru fereastra cea mai medie
class Ui_MedWindow(object):

    # setup UI
    def setupUi(self, MedWindow):

        #general style window MED
        MedWindow.setObjectName("MedWindow")
        MedWindow.setEnabled(True)
        MedWindow.resize(800, 600)
        MedWindow.setStyleSheet("background-color: rgb(130, 0, 124);")
        MedWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)

        #center
        self.centralwidget = QtWidgets.QWidget(MedWindow)
        self.centralwidget.setObjectName("centralwidget")

        #style frame (input si btn)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 450, 801, 80))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # input
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 401, 41))
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        #style font pushButton
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)

        #ask btn
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(520, 20, 141, 41))
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        #style fonts headText
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        #head title
        self.headText = QtWidgets.QLabel(self.centralwidget)
        self.headText.setGeometry(QtCore.QRect(0, 10, 801, 71))
        self.headText.setFont(font)
        self.headText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headText.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"font: 75 36pt \"Segoe Print\";")
        self.headText.setAlignment(QtCore.Qt.AlignCenter)
        self.headText.setObjectName("headText")

        #raspuns label
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(0, 370, 801, 51))
        self.answer.setStyleSheet("font: 63 16pt \"Open Sans\";\n"
"color: rgb(255, 255, 255);")
        self.answer.setScaledContents(False)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")

        #img style
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(200, 100, 381, 241))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("ball.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")

        MedWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MedWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        MedWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MedWindow)
        self.statusbar.setObjectName("statusbar")
        MedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MedWindow)
        QtCore.QMetaObject.connectSlotsByName(MedWindow)

    # retranslarea UI
    def retranslateUi(self, MedWindow):
        _translate = QtCore.QCoreApplication.translate
        MedWindow.setWindowTitle(_translate("MedWindow", "Magic 8 Ball"))
        MedWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pushButton.setText(_translate("MedWindow", "Ask"))
        self.headText.setText(_translate("MedWindow", "The Magic 8 Ball"))
        self.answer.setText(_translate("MedWindow", "Ai o intrebare?"))

#clasa p-tru fereastra cea mai mica
class Ui_MinWindow(object):

    # setup UI
    def setupUi(self, MinWindow):

        # general style window MIN
        MinWindow.setObjectName("MinWindow")
        MinWindow.setEnabled(True)
        MinWindow.resize(620, 400)
        MinWindow.setStyleSheet("background-color: rgb(130, 0, 124);")
        MinWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)

        #center
        self.centralwidget = QtWidgets.QWidget(MinWindow)
        self.centralwidget.setObjectName("centralwidget")

        # style frame (input si btn)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 290, 601, 51))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # input
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 321, 31))
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 87 italic 12pt \"Segoe UI Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        # style font pushButton
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)

        #ask btn
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(410, 10, 111, 31))
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        # style fonts headText
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)

        # head title
        self.headText = QtWidgets.QLabel(self.centralwidget)
        self.headText.setGeometry(QtCore.QRect(10, 10, 601, 41))
        self.headText.setFont(font)
        self.headText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.headText.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"font: 75 20pt \"Segoe Print\";")
        self.headText.setAlignment(QtCore.Qt.AlignCenter)
        self.headText.setObjectName("headText")

        # raspuns label
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(10, 250, 601, 21))
        self.answer.setStyleSheet("font: 63 14pt \"Open Sans\";\n"
"color: rgb(255, 255, 255);")
        self.answer.setScaledContents(False)
        self.answer.setAlignment(QtCore.Qt.AlignCenter)
        self.answer.setObjectName("answer")

        # img style
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(200, 70, 251, 161))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("ball.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")

        MinWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MinWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")

        MinWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MinWindow)
        self.statusbar.setObjectName("statusbar")

        MinWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MinWindow)
        QtCore.QMetaObject.connectSlotsByName(MinWindow)

    def retranslateUi(self, MinWindow):
        _translate = QtCore.QCoreApplication.translate
        MinWindow.setWindowTitle(_translate("MinWindow", "Magic 8 Ball"))
        MinWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.pushButton.setText(_translate("MinWindow", "Ask"))
        self.headText.setText(_translate("MinWindow", "The Magic 8 Ball"))
        self.answer.setText(_translate("MinWindow", "Ai o intrebare?"))

answers = [
        # Positive
        'Este sigur',
        'Este incontestabil',
        'Fără îndoială ',
        'Da - cu siguranţă ',
        'Puteţi să vă bazaţi pe ea',

        # Ezitant pozitiv
        'După cum văd eu lucrurile, da',
        'Outlook bun',
        'Punct de semne pentru a da',
        'Da',

        # Neutru
        'Răspuns neclar, încercaţi din nou',
        'Adresaţi-vă din nou mai târziu',
        'Mai bine nu-ţi spun acum',
        'Nu se poate prezice acum',
        'Se concentrează şi întreabă din nou',

        # Negativ
        'Nu conta pe el',
        'Răspunsul meu este nu',
        'Sursele mele spun că nu',
        'Perspectivele nu sunt atît de bune',
        'Foarte dubios'
    ]

#clasa logica a jocului
class MysticBall:
    def __init__(self):
        # Window
        self.app = QtWidgets.QApplication(sys.argv)
        self.Window = QtWidgets.QMainWindow()
        self.window = Ui_StartWindow()
        self.window.setupUi(self.Window)

        #btn start settings si exit spre scenele respective
        self.window.start.clicked.connect(self.medGame)
        self.window.settings.clicked.connect(self.showGameSettings)
        self.window.exit.clicked.connect(self.GameExit)

    #fereastra Game start
    def showGameStart(self):
        print("Game start")
        self.Window = QtWidgets.QMainWindow()
        self.window = Ui_MedWindow()
        self.window.setupUi(self.Window)
        self.Window.show()

    #fereastra setarilor
    def showGameSettings(self):
        print("Game Settings")
        self.Window = QtWidgets.QMainWindow()
        self.window = Ui_MainWindow()
        self.window.setupUi(self.Window)
        self.Window.show()

        # default radio checked
        self.window.radioButton_2Sett.setChecked(True)
        self.window.start.clicked.connect(self.medGame)

        #chose resolution radio
        self.window.radioButtonSett.clicked.connect(self.largeGame)
        self.window.radioButton_2Sett.clicked.connect(self.medGame)
        self.window.radioButton_3Sett.clicked.connect(self.minGame)

        # if self.window.radioButtonSett.isChecked() == True:
        #     self.window.start.clicked.connect(self.largeGame)
        #
        # elif self.window.radioButton_2Sett.isChecked() == True:
        #     self.window.start.clicked.connect(self.medGame)
        #
        # elif self.window.radioButton_2Sett.isChecked() == True:
        #     self.window.start.clicked.connect(self.minGame)

    #constructor p-tru window MIN
    def minGame(self):
        self.Window = QtWidgets.QMainWindow()
        self.window = Ui_MinWindow()
        self.window.setupUi(self.Window)
        self.Window.show()
        self.window.pushButton.clicked.connect(self.answersGame)

    # constructor p-tru window MED
    def medGame(self):
        self.Window = QtWidgets.QMainWindow()
        self.window = Ui_MedWindow()
        self.window.setupUi(self.Window)
        self.Window.show()
        self.window.pushButton.clicked.connect(self.answersGame)

    # constructor p-tru window LARGE
    def largeGame(self):
        self.Window = QtWidgets.QMainWindow()
        self.window = Ui_LargeWindow()
        self.window.setupUi(self.Window)
        self.Window.show()
        self.window.pushButton.clicked.connect(self.answersGame)

    #generarea unui nr aleator din lista answers
    def randNumberLi(self):
        return answers[random.randint(0, len(answers)-1)]

    #constructor logica intrebarilor
    def answersGame(self):
        if self.window.lineEdit.text() == '':
            self.window.answer.setText('Ai o intrebare?')
        else:
            answer = self.randNumberLi()
            time.sleep(1)
            self.window.answer.setText('Hmmmm... \n ' + answer)

    #constructor exit game
    def GameExit(self):
        self.Window.close()

    # constructor start game
    def start(self):
        self.Window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    game = MysticBall()
    game.start()