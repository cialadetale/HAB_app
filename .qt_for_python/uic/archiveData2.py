# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archiveData2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from map.map import mapWidget

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 737)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
" background-color: white\n"
"}\n"
"\n"
"#liveDataContainer, #archiveDataContainer{\n"
" background-color: #F4F4F4;\n"
" box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
" border-radius: 50px;\n"
"}\n"
"\n"
"#archiveDataBtn, #liveDataBtn{\n"
" background: #F8C65E;\n"
" box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
" border-radius: 30px;\n"
"}\n"
"\n"
"#settingsBtn, #infoBtn, #liveDataIcon, #archiveDataIcon, #returnBtn{\n"
" border: none;\n"
" background-color: transparent;\n"
"}\n"
"\n"
"#liveDataBtn:hover, #archiveDataBtn:hover{\n"
" border: none;\n"
" background-color: rgb(242, 157, 0);\n"
"}\n"
"\n"
"#addFile, #buttons, #missionDuration, #mapContainer {\n"
" background-color: #F4F4F4;\n"
" border-radius: 20px;\n"
"}\n"
"\n"
"#widget_2, #widget_7, #widget_8, #widget_9, #widget_13, #label_4, #label_5{\n"
" background-color: #F4F4F4;\n"
"}\n"
"\n"
"#uploadBtn {\n"
" background-color: #F8C65E;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#dataBtn, #chartsBtn {\n"
" background-color: #F8C65E;\n"
" border-radius"
                        ": 10px;\n"
"}\n"
"\n"
"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-10, 0, 1301, 751))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperContainer = QWidget(self.page)
        self.upperContainer.setObjectName(u"upperContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperContainer.sizePolicy().hasHeightForWidth())
        self.upperContainer.setSizePolicy(sizePolicy)
        self.upperContainer.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout = QHBoxLayout(self.upperContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.upperContainer)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.returnBtn = QPushButton(self.widget)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icons/yellow_pack/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.returnBtn.setIcon(icon)
        self.returnBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.returnBtn)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_3 = QWidget(self.upperContainer)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.superclusterLogo = QLabel(self.widget_3)
        self.superclusterLogo.setObjectName(u"superclusterLogo")
        self.superclusterLogo.setMinimumSize(QSize(110, 80))
        self.superclusterLogo.setMaximumSize(QSize(110, 80))
        self.superclusterLogo.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo.setScaledContents(True)
        self.superclusterLogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.superclusterLogo)


        self.horizontalLayout.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.widget_4 = QWidget(self.upperContainer)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.settingsBtn = QPushButton(self.widget_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(0, 50))
        self.settingsBtn.setMaximumSize(QSize(50, 50))
        self.settingsBtn.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/hover_icons/icons/hover/settings.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-repeat: no-repeat;\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/yellow_pack/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon1)
        self.settingsBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.widget_4)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(50, 50))
        self.infoBtn.setMaximumSize(QSize(50, 50))
        self.infoBtn.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/hover_icons/icons/hover/info.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-repeat: no-repeat;\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/hover_icons/icons/hover/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon2)
        self.infoBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.infoBtn)


        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.upperContainer)

        self.archiveDataLabel = QWidget(self.page)
        self.archiveDataLabel.setObjectName(u"archiveDataLabel")
        self.verticalLayout_13 = QVBoxLayout(self.archiveDataLabel)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_6 = QWidget(self.archiveDataLabel)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Inria Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_14 = QVBoxLayout(self.widget_11)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_11)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Inria Sans")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)

        self.verticalLayout_14.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_15 = QVBoxLayout(self.widget_12)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 0)
        self.label_6 = QLabel(self.widget_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_15.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.widget_12)


        self.verticalLayout_13.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.archiveDataLabel)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.widget_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)


        self.verticalLayout_13.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.archiveDataLabel)

        self.mainContainer = QWidget(self.page)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.mapContainer = QWidget(self.mainContainer)
        self.mapContainer.setObjectName(u"mapContainer")
        self.verticalLayout_2 = QVBoxLayout(self.mapContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.mapContainer)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Inria Sans")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.mapContainer)

        self.fileContainer = mapWidget(self.mainContainer)
        self.fileContainer.setObjectName(u"fileContainer")
        self.fileContainer.setMinimumSize(QSize(0, 0))
        self.fileContainer.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.fileContainer)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addFile = QWidget(self.fileContainer)
        self.addFile.setObjectName(u"addFile")
        self.verticalLayout_6 = QVBoxLayout(self.addFile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_7 = QWidget(self.addFile)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_8 = QVBoxLayout(self.widget_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Inria Sans")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.addFile)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.verticalLayout_11 = QVBoxLayout(self.widget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.widget_9)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QSize(600, 30))

        self.verticalLayout_11.addWidget(self.plainTextEdit)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.addFile)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.uploadBtn = QPushButton(self.widget_8)
        self.uploadBtn.setObjectName(u"uploadBtn")
        self.uploadBtn.setMinimumSize(QSize(100, 30))
        font4 = QFont()
        font4.setFamily(u"Inria Sans")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.uploadBtn.setFont(font4)

        self.verticalLayout_7.addWidget(self.uploadBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.addFile, 0, Qt.AlignTop)

        self.missionDuration = QWidget(self.fileContainer)
        self.missionDuration.setObjectName(u"missionDuration")
        self.verticalLayout_9 = QVBoxLayout(self.missionDuration)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_2 = QWidget(self.missionDuration)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.verticalLayout_10.addWidget(self.label_5)


        self.verticalLayout_9.addWidget(self.widget_2)

        self.widget_13 = QWidget(self.missionDuration)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_12 = QVBoxLayout(self.widget_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.plainTextEdit_2 = QPlainTextEdit(self.widget_13)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_2.setMaximumSize(QSize(600, 30))

        self.verticalLayout_12.addWidget(self.plainTextEdit_2)


        self.verticalLayout_9.addWidget(self.widget_13)


        self.verticalLayout_3.addWidget(self.missionDuration)

        self.buttons = QWidget(self.fileContainer)
        self.buttons.setObjectName(u"buttons")
        self.horizontalLayout_4 = QHBoxLayout(self.buttons)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.dataBtn = QPushButton(self.buttons)
        self.dataBtn.setObjectName(u"dataBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dataBtn.sizePolicy().hasHeightForWidth())
        self.dataBtn.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Inria Sans")
        font5.setPointSize(16)
        font5.setBold(False)
        font5.setWeight(50)
        self.dataBtn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.dataBtn)

        self.chartsBtn = QPushButton(self.buttons)
        self.chartsBtn.setObjectName(u"chartsBtn")
        sizePolicy2.setHeightForWidth(self.chartsBtn.sizePolicy().hasHeightForWidth())
        self.chartsBtn.setSizePolicy(sizePolicy2)
        self.chartsBtn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.chartsBtn)


        self.verticalLayout_3.addWidget(self.buttons)


        self.horizontalLayout_3.addWidget(self.fileContainer)


        self.verticalLayout.addWidget(self.mainContainer)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.returnBtn.setText("")
        self.superclusterLogo.setText("")
        self.settingsBtn.setText("")
        self.infoBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ARCHIVE DATA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"tu b\u0119dzie mapka", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select file:", None))
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mission duration:", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.chartsBtn.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
    # retranslateUi

