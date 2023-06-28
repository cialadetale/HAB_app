# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from map.map import mapWidget
from mplwidget import MplWidget

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1281, 729)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"*{\n"
" background-color: white\n"
"}\n"
"\n"
"#liveDataContainer, #archiveDataContainer{\n"
" background-color: #F4F4F4;\n"
" border-radius: 50px;\n"
"}\n"
"\n"
"#archiveDataBtn, #liveDataBtn{\n"
" background: #F8C65E;\n"
" border-radius: 30px;\n"
"}\n"
"\n"
"#settingsBtn, #infoBtn, #liveDataIcon, #archiveDataIcon, #returnBtn, #settingsBtn_2, #infoBtn_2, #settingsBtn_3, #infoBtn_3, #returnBtn_2, #settingsBtn_4, #infoBtn_4, #returnBtn_3, #settingsBtn_5, #infoBtn_5, #returnBtn_4, #settingsBtn_6, #infoBtn_6, #returnBtn_5, #settingsBtn_7, #infoBtn_7, #returnBtn_6, #settingsBtn_8, #infoBtn_8, #returnBtn_7 {\n"
" border: none;\n"
" background-color: transparent;\n"
"}\n"
"\n"
"#liveDataBtn:hover, #archiveDataBtn:hover{\n"
" border: none;\n"
" background-color: rgb(242, 157, 0);\n"
"}\n"
"\n"
"#addFile, #buttons, #missionDuration, #mapContainer, #bluetoothWidget,  #loraWidget,#buttons_2, #pressureButton, #outsideTempBtn, #tempBmpBtn, #difPressureBtn, #hscTempBtn, #windNsBtn, #windWeBtn, #axBtn, #ayBtn, #azBtn, #angP"
                        "Btn, #angQBtn, #angRBtn, #hxBtn, #hyBtn, #hzBtn,#radDioBtn, #geigBtn, #iUseBtn, #batVBtn, #gpsSpeedBtn, #gpsTrackBtn, #satNumBtn, #gpsAltBtn {\n"
" background-color: #F4F4F4;\n"
" border-radius: 20px;\n"
"}\n"
"\n"
"#rtnBtnPg2, #voidBtn8, #voidRtnBtn, #nxtPgBtn1, #rtnBtnPg1, #fwdBtnPg3 {\n"
" background-color: #F4F4F4;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"#pressureButton:hover, #outsideTempBtn:hover, #tempBmpBtn:hover, #difPressureBtn:hover, #hscTempBtn:hover, #windNsBtn:hover, #windWeBtn:hover, #axBtn:hover, #ayBtn:hover, #azBtn:hover, #rtnBtnPg2:hover, #voidBtn8:hover, #voidRtnBtn:hover, #nxtPgBtn1:hover, #rtnBtnPg1:hover, #fwdBtnPg3:hover, #angPBtn:hover, #angQBtn:hover, #angRBtn:hover, #hxBtn:hover, #hyBtn:hover, #hzBtn:hover, #radDioBtn:hover, #geigBtn:hover, #iUseBtn:hover, #batVBtn:hover, #gpsSpeedBtn:hover, #gpsTrackBtn:hover, #satNumBtn:hover, #gpsAltBtn:hover {\n"
" border: none;\n"
" background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
"#widget_2, #widget_7, #widget_8, #widget_9, #widget_13, #lab"
                        "el_4, #label_5, #widget_3, #label_10, #widget_17, #label_9, #widget_19,#widget_20,#widget_21{\n"
" background-color: #F4F4F4;\n"
"}\n"
"\n"
"#uploadBtn {\n"
" background-color: #F8C65E;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#dataBtn, #chartsBtn, #dataBtn_2, #chartsBtn_2,  #connectBtn {\n"
" background-color: #F8C65E;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"#dataBtn:hover, #chartsBtn:hover, #uploadBtn:hover, #dataBtn_2:hover, #chartsBtn_2:hover, #connectBtn:hover{\n"
" border: none;\n"
" background-color: rgb(242, 157, 0);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"            border: 0px solid #999999;\n"
"            background:white;   \n"
"			height:8px; \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"\n"
"        QScrollBar::handle {         \n"
"       \n"
"            min-height: 0px;\n"
"          	border: 0px solid red;\n"
"			border-radius: 4px;\n"
"			background-color: rgb(151, 151, 151);\n"
"        }\n"
"\n"
"\n"
"QHeaderView::section {   \n"
"    \n"
"    background-color:  rgb("
                        "225, 225, 225);\n"
"    border-width: 1px 0px 1px 1px;\n"
"    border-style: solid;\n"
"    border-color: white;\n"
"  \n"
"    min-height:3em;\n"
"    \n"
"	\n"
"}\n"
"\n"
"QTableWidget { \n"
"  background-color:  white;\n"
"  gridline-color:rgb(225, 225, 225);\n"
"  border-style: none;\n"
"}\n"
"\n"
"\n"
"*{selection-background-color: rgb(250, 184, 96);}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.archiveData = QWidget()
        self.archiveData.setObjectName(u"archiveData")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.archiveData.sizePolicy().hasHeightForWidth())
        self.archiveData.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.archiveData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperContainer = QWidget(self.archiveData)
        self.upperContainer.setObjectName(u"upperContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.upperContainer.sizePolicy().hasHeightForWidth())
        self.upperContainer.setSizePolicy(sizePolicy3)
        self.upperContainer.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout = QHBoxLayout(self.upperContainer)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer = QWidget(self.upperContainer)
        self.leftSubContainer.setObjectName(u"leftSubContainer")
        self.horizontalLayout_2 = QHBoxLayout(self.leftSubContainer)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.returnBtn = QPushButton(self.leftSubContainer)
        self.returnBtn.setObjectName(u"returnBtn")
        self.returnBtn.setMaximumSize(QSize(100, 100))
        icon = QIcon()
        icon.addFile(u":/icons/icons/yellow_pack/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.returnBtn.setIcon(icon)
        self.returnBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.returnBtn)


        self.horizontalLayout.addWidget(self.leftSubContainer, 0, Qt.AlignLeft)

        self.midSubContainer = QWidget(self.upperContainer)
        self.midSubContainer.setObjectName(u"midSubContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.midSubContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.superclusterLogo = QLabel(self.midSubContainer)
        self.superclusterLogo.setObjectName(u"superclusterLogo")
        self.superclusterLogo.setMinimumSize(QSize(110, 80))
        self.superclusterLogo.setMaximumSize(QSize(110, 80))
        self.superclusterLogo.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo.setScaledContents(True)
        self.superclusterLogo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.superclusterLogo)


        self.horizontalLayout.addWidget(self.midSubContainer, 0, Qt.AlignHCenter)

        self.rightSubContainer = QWidget(self.upperContainer)
        self.rightSubContainer.setObjectName(u"rightSubContainer")
        self.horizontalLayout_6 = QHBoxLayout(self.rightSubContainer)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn = QPushButton(self.rightSubContainer)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(0, 50))
        self.settingsBtn.setMaximumSize(QSize(50, 50))
        self.settingsBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/yellow_pack/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon1)
        self.settingsBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.rightSubContainer)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(50, 50))
        self.infoBtn.setMaximumSize(QSize(100, 100))
        self.infoBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/yellow_pack/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon2)
        self.infoBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.infoBtn)


        self.horizontalLayout.addWidget(self.rightSubContainer, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.upperContainer)

        self.archiveDataLabel = QWidget(self.archiveData)
        self.archiveDataLabel.setObjectName(u"archiveDataLabel")
        self.verticalLayout_13 = QVBoxLayout(self.archiveDataLabel)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pageTitleWidget = QWidget(self.archiveDataLabel)
        self.pageTitleWidget.setObjectName(u"pageTitleWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.pageTitleWidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.pageTitleWidget)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_5 = QVBoxLayout(self.widget_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.missionLabel = QLabel(self.widget_10)
        self.missionLabel.setObjectName(u"missionLabel")
        font = QFont()
        font.setFamily(u"Inria Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.missionLabel.setFont(font)

        self.verticalLayout_5.addWidget(self.missionLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.titleLabel = QWidget(self.pageTitleWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.verticalLayout_14 = QVBoxLayout(self.titleLabel)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.titleLabel)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Inria Sans")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)

        self.verticalLayout_14.addWidget(self.label, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.titleLabel)

        self.widget_12 = QWidget(self.pageTitleWidget)
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


        self.verticalLayout_13.addWidget(self.pageTitleWidget)

        self.separatorWidget = QWidget(self.archiveDataLabel)
        self.separatorWidget.setObjectName(u"separatorWidget")
        self.verticalLayout_4 = QVBoxLayout(self.separatorWidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.separatorWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)


        self.verticalLayout_13.addWidget(self.separatorWidget)


        self.verticalLayout.addWidget(self.archiveDataLabel)

        self.mainContainer = QWidget(self.archiveData)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.mapWidget = mapWidget(self.mainContainer)
        self.mapWidget.setObjectName(u"mapWidget")
        sizePolicy2.setHeightForWidth(self.mapWidget.sizePolicy().hasHeightForWidth())
        self.mapWidget.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.mapWidget)

        self.fileContainer = QWidget(self.mainContainer)
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
        font2 = QFont()
        font2.setFamily(u"Inria Sans")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.addFile)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.widget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.filePathLabel = QLabel(self.widget_9)
        self.filePathLabel.setObjectName(u"filePathLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.filePathLabel.sizePolicy().hasHeightForWidth())
        self.filePathLabel.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setFamily(u"Inria Sans")
        font3.setPointSize(12)
        self.filePathLabel.setFont(font3)
        self.filePathLabel.setMouseTracking(False)
        self.filePathLabel.setFocusPolicy(Qt.ClickFocus)
        self.filePathLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.filePathLabel.setMargin(5)
        self.filePathLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_11.addWidget(self.filePathLabel)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.addFile)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.uploadBtn = QPushButton(self.widget_8)
        self.uploadBtn.setObjectName(u"uploadBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.uploadBtn.sizePolicy().hasHeightForWidth())
        self.uploadBtn.setSizePolicy(sizePolicy5)
        self.uploadBtn.setMinimumSize(QSize(150, 30))
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
        self.label_5.setFont(font2)

        self.verticalLayout_10.addWidget(self.label_5)


        self.verticalLayout_9.addWidget(self.widget_2)

        self.widget_13 = QWidget(self.missionDuration)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_12 = QVBoxLayout(self.widget_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.missionParamLabel = QPlainTextEdit(self.widget_13)
        self.missionParamLabel.setObjectName(u"missionParamLabel")
        self.missionParamLabel.setMinimumSize(QSize(0, 0))
        self.missionParamLabel.setMaximumSize(QSize(600, 30))

        self.verticalLayout_12.addWidget(self.missionParamLabel)


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
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dataBtn.sizePolicy().hasHeightForWidth())
        self.dataBtn.setSizePolicy(sizePolicy6)
        font5 = QFont()
        font5.setFamily(u"Inria Sans")
        font5.setPointSize(16)
        font5.setBold(False)
        font5.setWeight(50)
        self.dataBtn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.dataBtn)

        self.chartsBtn = QPushButton(self.buttons)
        self.chartsBtn.setObjectName(u"chartsBtn")
        sizePolicy6.setHeightForWidth(self.chartsBtn.sizePolicy().hasHeightForWidth())
        self.chartsBtn.setSizePolicy(sizePolicy6)
        self.chartsBtn.setFont(font5)

        self.horizontalLayout_4.addWidget(self.chartsBtn)


        self.verticalLayout_3.addWidget(self.buttons)


        self.horizontalLayout_3.addWidget(self.fileContainer)


        self.verticalLayout.addWidget(self.mainContainer)

        self.stackedWidget.addWidget(self.archiveData)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        sizePolicy2.setHeightForWidth(self.mainPage.sizePolicy().hasHeightForWidth())
        self.mainPage.setSizePolicy(sizePolicy2)
        self.verticalLayout_18 = QVBoxLayout(self.mainPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.upperContainer_2 = QWidget(self.mainPage)
        self.upperContainer_2.setObjectName(u"upperContainer_2")
        sizePolicy3.setHeightForWidth(self.upperContainer_2.sizePolicy().hasHeightForWidth())
        self.upperContainer_2.setSizePolicy(sizePolicy3)
        self.upperContainer_2.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_9 = QHBoxLayout(self.upperContainer_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_2 = QWidget(self.upperContainer_2)
        self.leftSubContainer_2.setObjectName(u"leftSubContainer_2")
        self.horizontalLayout_10 = QHBoxLayout(self.leftSubContainer_2)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, -1, 20, -1)

        self.horizontalLayout_9.addWidget(self.leftSubContainer_2)

        self.midSubContainer_2 = QWidget(self.upperContainer_2)
        self.midSubContainer_2.setObjectName(u"midSubContainer_2")
        self.horizontalLayout_11 = QHBoxLayout(self.midSubContainer_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.superclusterLogo_2 = QLabel(self.midSubContainer_2)
        self.superclusterLogo_2.setObjectName(u"superclusterLogo_2")
        self.superclusterLogo_2.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_2.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_2.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_2.setScaledContents(True)
        self.superclusterLogo_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.superclusterLogo_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.midSubContainer_2, 0, Qt.AlignHCenter)

        self.rightSubContainer_2 = QWidget(self.upperContainer_2)
        self.rightSubContainer_2.setObjectName(u"rightSubContainer_2")
        self.horizontalLayout_12 = QHBoxLayout(self.rightSubContainer_2)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_2 = QPushButton(self.rightSubContainer_2)
        self.settingsBtn_2.setObjectName(u"settingsBtn_2")
        self.settingsBtn_2.setMinimumSize(QSize(0, 50))
        self.settingsBtn_2.setMaximumSize(QSize(50, 50))
        self.settingsBtn_2.setStyleSheet(u"")
        self.settingsBtn_2.setIcon(icon1)
        self.settingsBtn_2.setIconSize(QSize(50, 50))

        self.horizontalLayout_12.addWidget(self.settingsBtn_2)

        self.infoBtn_2 = QPushButton(self.rightSubContainer_2)
        self.infoBtn_2.setObjectName(u"infoBtn_2")
        self.infoBtn_2.setMinimumSize(QSize(50, 50))
        self.infoBtn_2.setMaximumSize(QSize(50, 50))
        self.infoBtn_2.setStyleSheet(u"")
        self.infoBtn_2.setIcon(icon2)
        self.infoBtn_2.setIconSize(QSize(50, 50))

        self.horizontalLayout_12.addWidget(self.infoBtn_2)


        self.horizontalLayout_9.addWidget(self.rightSubContainer_2, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.upperContainer_2, 0, Qt.AlignTop)

        self.homePageLabel = QWidget(self.mainPage)
        self.homePageLabel.setObjectName(u"homePageLabel")
        sizePolicy.setHeightForWidth(self.homePageLabel.sizePolicy().hasHeightForWidth())
        self.homePageLabel.setSizePolicy(sizePolicy)
        self.verticalLayout_19 = QVBoxLayout(self.homePageLabel)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_14 = QWidget(self.homePageLabel)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_21 = QVBoxLayout(self.widget_16)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_16)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_21.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.widget_16)


        self.verticalLayout_19.addWidget(self.widget_14)

        self.widget_18 = QWidget(self.homePageLabel)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_23 = QVBoxLayout(self.widget_18)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.widget_18)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_2)


        self.verticalLayout_19.addWidget(self.widget_18)


        self.verticalLayout_18.addWidget(self.homePageLabel, 0, Qt.AlignTop)

        self.homeMainContainer = QWidget(self.mainPage)
        self.homeMainContainer.setObjectName(u"homeMainContainer")
        sizePolicy.setHeightForWidth(self.homeMainContainer.sizePolicy().hasHeightForWidth())
        self.homeMainContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout_8 = QHBoxLayout(self.homeMainContainer)
        self.horizontalLayout_8.setSpacing(100)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, 50, 50, 50)
        self.liveDataContainer = QWidget(self.homeMainContainer)
        self.liveDataContainer.setObjectName(u"liveDataContainer")
        sizePolicy.setHeightForWidth(self.liveDataContainer.sizePolicy().hasHeightForWidth())
        self.liveDataContainer.setSizePolicy(sizePolicy)
        self.liveDataContainer.setMaximumSize(QSize(900, 600))
        self.verticalLayout_16 = QVBoxLayout(self.liveDataContainer)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(30, 30, 30, 30)
        self.liveDataIcon = QLabel(self.liveDataContainer)
        self.liveDataIcon.setObjectName(u"liveDataIcon")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.liveDataIcon.sizePolicy().hasHeightForWidth())
        self.liveDataIcon.setSizePolicy(sizePolicy7)
        self.liveDataIcon.setMaximumSize(QSize(16777215, 16777215))
        self.liveDataIcon.setPixmap(QPixmap(u":/pixmap/icons/pin.png"))
        self.liveDataIcon.setScaledContents(False)
        self.liveDataIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.liveDataIcon, 0, Qt.AlignHCenter)

        self.liveDataBtn = QPushButton(self.liveDataContainer)
        self.liveDataBtn.setObjectName(u"liveDataBtn")
        self.liveDataBtn.setMinimumSize(QSize(300, 80))
        font6 = QFont()
        font6.setFamily(u"Inria Sans")
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setWeight(50)
        self.liveDataBtn.setFont(font6)

        self.verticalLayout_16.addWidget(self.liveDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.liveDataContainer)

        self.archiveDataContainer = QWidget(self.homeMainContainer)
        self.archiveDataContainer.setObjectName(u"archiveDataContainer")
        sizePolicy.setHeightForWidth(self.archiveDataContainer.sizePolicy().hasHeightForWidth())
        self.archiveDataContainer.setSizePolicy(sizePolicy)
        self.archiveDataContainer.setMaximumSize(QSize(900, 600))
        self.verticalLayout_17 = QVBoxLayout(self.archiveDataContainer)
        self.verticalLayout_17.setSpacing(20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(30, 30, 30, 30)
        self.archiveDataIcon = QLabel(self.archiveDataContainer)
        self.archiveDataIcon.setObjectName(u"archiveDataIcon")
        sizePolicy7.setHeightForWidth(self.archiveDataIcon.sizePolicy().hasHeightForWidth())
        self.archiveDataIcon.setSizePolicy(sizePolicy7)
        self.archiveDataIcon.setMaximumSize(QSize(16777215, 16777215))
        self.archiveDataIcon.setPixmap(QPixmap(u":/pixmap/icons/plot.png"))
        self.archiveDataIcon.setScaledContents(False)
        self.archiveDataIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.archiveDataIcon, 0, Qt.AlignHCenter)

        self.archiveDataBtn = QPushButton(self.archiveDataContainer)
        self.archiveDataBtn.setObjectName(u"archiveDataBtn")
        sizePolicy7.setHeightForWidth(self.archiveDataBtn.sizePolicy().hasHeightForWidth())
        self.archiveDataBtn.setSizePolicy(sizePolicy7)
        self.archiveDataBtn.setMinimumSize(QSize(300, 80))
        font7 = QFont()
        font7.setFamily(u"Inria Sans")
        font7.setPointSize(18)
        self.archiveDataBtn.setFont(font7)

        self.verticalLayout_17.addWidget(self.archiveDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.archiveDataContainer)


        self.verticalLayout_18.addWidget(self.homeMainContainer, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.mainPage)
        self.liveData = QWidget()
        self.liveData.setObjectName(u"liveData")
        sizePolicy2.setHeightForWidth(self.liveData.sizePolicy().hasHeightForWidth())
        self.liveData.setSizePolicy(sizePolicy2)
        self.verticalLayout_36 = QVBoxLayout(self.liveData)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.upperContainer_3 = QWidget(self.liveData)
        self.upperContainer_3.setObjectName(u"upperContainer_3")
        sizePolicy3.setHeightForWidth(self.upperContainer_3.sizePolicy().hasHeightForWidth())
        self.upperContainer_3.setSizePolicy(sizePolicy3)
        self.upperContainer_3.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_14 = QHBoxLayout(self.upperContainer_3)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_3 = QWidget(self.upperContainer_3)
        self.leftSubContainer_3.setObjectName(u"leftSubContainer_3")
        self.horizontalLayout_15 = QHBoxLayout(self.leftSubContainer_3)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, -1, 20, -1)
        self.returnBtn_2 = QPushButton(self.leftSubContainer_3)
        self.returnBtn_2.setObjectName(u"returnBtn_2")
        self.returnBtn_2.setMaximumSize(QSize(100, 100))
        self.returnBtn_2.setIcon(icon)
        self.returnBtn_2.setIconSize(QSize(50, 50))

        self.horizontalLayout_15.addWidget(self.returnBtn_2)


        self.horizontalLayout_14.addWidget(self.leftSubContainer_3, 0, Qt.AlignLeft)

        self.midSubContainer_3 = QWidget(self.upperContainer_3)
        self.midSubContainer_3.setObjectName(u"midSubContainer_3")
        self.horizontalLayout_16 = QHBoxLayout(self.midSubContainer_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.superclusterLogo_3 = QLabel(self.midSubContainer_3)
        self.superclusterLogo_3.setObjectName(u"superclusterLogo_3")
        self.superclusterLogo_3.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_3.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_3.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_3.setScaledContents(True)
        self.superclusterLogo_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.superclusterLogo_3)


        self.horizontalLayout_14.addWidget(self.midSubContainer_3, 0, Qt.AlignHCenter)

        self.rightSubContainer_3 = QWidget(self.upperContainer_3)
        self.rightSubContainer_3.setObjectName(u"rightSubContainer_3")
        self.horizontalLayout_17 = QHBoxLayout(self.rightSubContainer_3)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_3 = QPushButton(self.rightSubContainer_3)
        self.settingsBtn_3.setObjectName(u"settingsBtn_3")
        self.settingsBtn_3.setMinimumSize(QSize(0, 50))
        self.settingsBtn_3.setMaximumSize(QSize(50, 50))
        self.settingsBtn_3.setStyleSheet(u"")
        self.settingsBtn_3.setIcon(icon1)
        self.settingsBtn_3.setIconSize(QSize(50, 50))

        self.horizontalLayout_17.addWidget(self.settingsBtn_3)

        self.infoBtn_3 = QPushButton(self.rightSubContainer_3)
        self.infoBtn_3.setObjectName(u"infoBtn_3")
        self.infoBtn_3.setMinimumSize(QSize(50, 50))
        self.infoBtn_3.setMaximumSize(QSize(100, 100))
        self.infoBtn_3.setStyleSheet(u"")
        self.infoBtn_3.setIcon(icon2)
        self.infoBtn_3.setIconSize(QSize(50, 50))

        self.horizontalLayout_17.addWidget(self.infoBtn_3)


        self.horizontalLayout_14.addWidget(self.rightSubContainer_3, 0, Qt.AlignRight)


        self.verticalLayout_36.addWidget(self.upperContainer_3)

        self.liveDataLabel = QWidget(self.liveData)
        self.liveDataLabel.setObjectName(u"liveDataLabel")
        self.verticalLayout_20 = QVBoxLayout(self.liveDataLabel)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pageTitleWidget_2 = QWidget(self.liveDataLabel)
        self.pageTitleWidget_2.setObjectName(u"pageTitleWidget_2")
        self.horizontalLayout_18 = QHBoxLayout(self.pageTitleWidget_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.pageTitleWidget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_22 = QVBoxLayout(self.widget_11)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 10, 0, 0)
        self.missionLabel_2 = QLabel(self.widget_11)
        self.missionLabel_2.setObjectName(u"missionLabel_2")
        self.missionLabel_2.setFont(font)

        self.verticalLayout_22.addWidget(self.missionLabel_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_18.addWidget(self.widget_11)

        self.titleLabel_2 = QWidget(self.pageTitleWidget_2)
        self.titleLabel_2.setObjectName(u"titleLabel_2")
        self.verticalLayout_24 = QVBoxLayout(self.titleLabel_2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.titleLabel_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_24.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_18.addWidget(self.titleLabel_2)

        self.widget_15 = QWidget(self.pageTitleWidget_2)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_25 = QVBoxLayout(self.widget_15)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 10, 0, 0)
        self.label_7 = QLabel(self.widget_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_25.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.horizontalLayout_18.addWidget(self.widget_15)


        self.verticalLayout_20.addWidget(self.pageTitleWidget_2)

        self.separatorWidget_2 = QWidget(self.liveDataLabel)
        self.separatorWidget_2.setObjectName(u"separatorWidget_2")
        self.verticalLayout_26 = QVBoxLayout(self.separatorWidget_2)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.separatorWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_3)


        self.verticalLayout_20.addWidget(self.separatorWidget_2)


        self.verticalLayout_36.addWidget(self.liveDataLabel)

        self.mainContainer_2 = QWidget(self.liveData)
        self.mainContainer_2.setObjectName(u"mainContainer_2")
        sizePolicy.setHeightForWidth(self.mainContainer_2.sizePolicy().hasHeightForWidth())
        self.mainContainer_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_19 = QHBoxLayout(self.mainContainer_2)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 10, 10, 10)
        self.mapWidget_2 = mapWidget(self.mainContainer_2)
        self.mapWidget_2.setObjectName(u"mapWidget_2")

        self.horizontalLayout_19.addWidget(self.mapWidget_2)

        self.connectionContainer = QWidget(self.mainContainer_2)
        self.connectionContainer.setObjectName(u"connectionContainer")
        self.connectionContainer.setMinimumSize(QSize(0, 0))
        self.connectionContainer.setMaximumSize(QSize(450, 16777215))
        self.verticalLayout_28 = QVBoxLayout(self.connectionContainer)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.bluetoothWidget = QWidget(self.connectionContainer)
        self.bluetoothWidget.setObjectName(u"bluetoothWidget")
        self.verticalLayout_29 = QVBoxLayout(self.bluetoothWidget)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_17 = QWidget(self.bluetoothWidget)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.widget_17)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_9 = QLabel(self.widget_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_30.addWidget(self.label_9)


        self.verticalLayout_29.addWidget(self.widget_17)

        self.widget_19 = QWidget(self.bluetoothWidget)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.verticalLayout_31 = QVBoxLayout(self.widget_19)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.filePathLabel_2 = QPlainTextEdit(self.widget_19)
        self.filePathLabel_2.setObjectName(u"filePathLabel_2")
        self.filePathLabel_2.setMinimumSize(QSize(0, 0))
        self.filePathLabel_2.setMaximumSize(QSize(600, 30))

        self.verticalLayout_31.addWidget(self.filePathLabel_2)


        self.verticalLayout_29.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.bluetoothWidget)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_32 = QVBoxLayout(self.widget_20)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.connectBtn = QPushButton(self.widget_20)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setMinimumSize(QSize(100, 30))
        self.connectBtn.setFont(font4)

        self.verticalLayout_32.addWidget(self.connectBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_29.addWidget(self.widget_20)


        self.verticalLayout_28.addWidget(self.bluetoothWidget, 0, Qt.AlignTop)

        self.loraWidget = QWidget(self.connectionContainer)
        self.loraWidget.setObjectName(u"loraWidget")
        self.verticalLayout_33 = QVBoxLayout(self.loraWidget)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_3 = QWidget(self.loraWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_34 = QVBoxLayout(self.widget_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_34.addWidget(self.label_10)


        self.verticalLayout_33.addWidget(self.widget_3)

        self.widget_21 = QWidget(self.loraWidget)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_35 = QVBoxLayout(self.widget_21)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.missionParamLabel_2 = QPlainTextEdit(self.widget_21)
        self.missionParamLabel_2.setObjectName(u"missionParamLabel_2")
        self.missionParamLabel_2.setMinimumSize(QSize(0, 0))
        self.missionParamLabel_2.setMaximumSize(QSize(600, 30))

        self.verticalLayout_35.addWidget(self.missionParamLabel_2)


        self.verticalLayout_33.addWidget(self.widget_21)


        self.verticalLayout_28.addWidget(self.loraWidget)

        self.buttons_2 = QWidget(self.connectionContainer)
        self.buttons_2.setObjectName(u"buttons_2")
        self.horizontalLayout_20 = QHBoxLayout(self.buttons_2)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, 20, 20, 20)
        self.dataBtn_2 = QPushButton(self.buttons_2)
        self.dataBtn_2.setObjectName(u"dataBtn_2")
        sizePolicy6.setHeightForWidth(self.dataBtn_2.sizePolicy().hasHeightForWidth())
        self.dataBtn_2.setSizePolicy(sizePolicy6)
        self.dataBtn_2.setFont(font5)

        self.horizontalLayout_20.addWidget(self.dataBtn_2)

        self.chartsBtn_2 = QPushButton(self.buttons_2)
        self.chartsBtn_2.setObjectName(u"chartsBtn_2")
        sizePolicy6.setHeightForWidth(self.chartsBtn_2.sizePolicy().hasHeightForWidth())
        self.chartsBtn_2.setSizePolicy(sizePolicy6)
        self.chartsBtn_2.setFont(font5)

        self.horizontalLayout_20.addWidget(self.chartsBtn_2)


        self.verticalLayout_28.addWidget(self.buttons_2)


        self.horizontalLayout_19.addWidget(self.connectionContainer)


        self.verticalLayout_36.addWidget(self.mainContainer_2)

        self.stackedWidget.addWidget(self.liveData)
        self.dataTablePage = QWidget()
        self.dataTablePage.setObjectName(u"dataTablePage")
        self.verticalLayout_27 = QVBoxLayout(self.dataTablePage)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.upperContainer_4 = QWidget(self.dataTablePage)
        self.upperContainer_4.setObjectName(u"upperContainer_4")
        sizePolicy3.setHeightForWidth(self.upperContainer_4.sizePolicy().hasHeightForWidth())
        self.upperContainer_4.setSizePolicy(sizePolicy3)
        self.upperContainer_4.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_21 = QHBoxLayout(self.upperContainer_4)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_4 = QWidget(self.upperContainer_4)
        self.leftSubContainer_4.setObjectName(u"leftSubContainer_4")
        self.horizontalLayout_22 = QHBoxLayout(self.leftSubContainer_4)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(20, -1, 20, -1)
        self.returnBtn_3 = QPushButton(self.leftSubContainer_4)
        self.returnBtn_3.setObjectName(u"returnBtn_3")
        self.returnBtn_3.setMaximumSize(QSize(100, 100))
        self.returnBtn_3.setIcon(icon)
        self.returnBtn_3.setIconSize(QSize(50, 50))

        self.horizontalLayout_22.addWidget(self.returnBtn_3)


        self.horizontalLayout_21.addWidget(self.leftSubContainer_4, 0, Qt.AlignLeft)

        self.midSubContainer_4 = QWidget(self.upperContainer_4)
        self.midSubContainer_4.setObjectName(u"midSubContainer_4")
        self.horizontalLayout_23 = QHBoxLayout(self.midSubContainer_4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.superclusterLogo_4 = QLabel(self.midSubContainer_4)
        self.superclusterLogo_4.setObjectName(u"superclusterLogo_4")
        self.superclusterLogo_4.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_4.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_4.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_4.setScaledContents(True)
        self.superclusterLogo_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.superclusterLogo_4)


        self.horizontalLayout_21.addWidget(self.midSubContainer_4, 0, Qt.AlignHCenter)

        self.rightSubContainer_4 = QWidget(self.upperContainer_4)
        self.rightSubContainer_4.setObjectName(u"rightSubContainer_4")
        self.horizontalLayout_24 = QHBoxLayout(self.rightSubContainer_4)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_4 = QPushButton(self.rightSubContainer_4)
        self.settingsBtn_4.setObjectName(u"settingsBtn_4")
        self.settingsBtn_4.setMinimumSize(QSize(0, 50))
        self.settingsBtn_4.setMaximumSize(QSize(50, 50))
        self.settingsBtn_4.setStyleSheet(u"")
        self.settingsBtn_4.setIcon(icon1)
        self.settingsBtn_4.setIconSize(QSize(50, 50))

        self.horizontalLayout_24.addWidget(self.settingsBtn_4)

        self.infoBtn_4 = QPushButton(self.rightSubContainer_4)
        self.infoBtn_4.setObjectName(u"infoBtn_4")
        self.infoBtn_4.setMinimumSize(QSize(50, 50))
        self.infoBtn_4.setMaximumSize(QSize(100, 100))
        self.infoBtn_4.setStyleSheet(u"")
        self.infoBtn_4.setIcon(icon2)
        self.infoBtn_4.setIconSize(QSize(50, 50))

        self.horizontalLayout_24.addWidget(self.infoBtn_4)


        self.horizontalLayout_21.addWidget(self.rightSubContainer_4, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.upperContainer_4)

        self.archiveDataLabel_2 = QWidget(self.dataTablePage)
        self.archiveDataLabel_2.setObjectName(u"archiveDataLabel_2")
        self.verticalLayout_41 = QVBoxLayout(self.archiveDataLabel_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.widget_26 = QWidget(self.archiveDataLabel_2)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_26 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.verticalLayout_42 = QVBoxLayout(self.widget_27)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 10, 0, 0)
        self.label_13 = QLabel(self.widget_27)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_42.addWidget(self.label_13, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.verticalLayout_43 = QVBoxLayout(self.widget_28)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_43.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_26)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_44 = QVBoxLayout(self.widget_29)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 10, 0, 0)
        self.label_15 = QLabel(self.widget_29)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_44.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.horizontalLayout_26.addWidget(self.widget_29)


        self.verticalLayout_41.addWidget(self.widget_26)

        self.widget_30 = QWidget(self.archiveDataLabel_2)
        self.widget_30.setObjectName(u"widget_30")
        self.verticalLayout_45 = QVBoxLayout(self.widget_30)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.line_5 = QFrame(self.widget_30)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_5)


        self.verticalLayout_41.addWidget(self.widget_30)


        self.verticalLayout_27.addWidget(self.archiveDataLabel_2)

        self.mainContainer_3 = QWidget(self.dataTablePage)
        self.mainContainer_3.setObjectName(u"mainContainer_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.mainContainer_3.sizePolicy().hasHeightForWidth())
        self.mainContainer_3.setSizePolicy(sizePolicy8)
        self.verticalLayout_46 = QVBoxLayout(self.mainContainer_3)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(20, 20, 20, 20)
        self.tableWidget = QTableWidget(self.mainContainer_3)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setFamily(u"Inria Sans")
        font8.setPointSize(9)
        font8.setBold(False)
        font8.setWeight(50)
        self.tableWidget.setFont(font8)
        self.tableWidget.setStyleSheet(u"QScrollBar:vertical {\n"
"            border: 0px solid #999999;\n"
"            background:white;\n"
"            width:8px;    \n"
"            margin: 10px 0px 0px 10px;\n"
"        }\n"
"\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"          	border: 0px solid red;\n"
"			border-radius: 4px;\n"
"			background-color: #F8C65E;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 2px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
"QScrollBar:horizontal {\n"
"            border: 0px solid #999999;\n"
"            background:white;   \n"
"			height:8px; \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {         \n"
"       \n"
"            min-height: 0px;\n"
"          	border: 0px solid red;\n"
"			border-radius: 4px;\n"
"			background-color: rgb(151, 151, 151);\n"
"        }\n"
"\n"
"\n"
"\n"
"*{s"
                        "election-background-color: rgb(250, 184, 96);}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(119)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_46.addWidget(self.tableWidget, 0, Qt.AlignLeft)


        self.verticalLayout_27.addWidget(self.mainContainer_3, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.dataTablePage)
        self.dataChartsPage = QWidget()
        self.dataChartsPage.setObjectName(u"dataChartsPage")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.dataChartsPage.sizePolicy().hasHeightForWidth())
        self.dataChartsPage.setSizePolicy(sizePolicy9)
        self.verticalLayout_49 = QVBoxLayout(self.dataChartsPage)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.upperContainer_5 = QWidget(self.dataChartsPage)
        self.upperContainer_5.setObjectName(u"upperContainer_5")
        sizePolicy3.setHeightForWidth(self.upperContainer_5.sizePolicy().hasHeightForWidth())
        self.upperContainer_5.setSizePolicy(sizePolicy3)
        self.upperContainer_5.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_25 = QHBoxLayout(self.upperContainer_5)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_5 = QWidget(self.upperContainer_5)
        self.leftSubContainer_5.setObjectName(u"leftSubContainer_5")
        self.horizontalLayout_27 = QHBoxLayout(self.leftSubContainer_5)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(20, -1, 20, -1)
        self.returnBtn_4 = QPushButton(self.leftSubContainer_5)
        self.returnBtn_4.setObjectName(u"returnBtn_4")
        self.returnBtn_4.setMaximumSize(QSize(100, 100))
        self.returnBtn_4.setIcon(icon)
        self.returnBtn_4.setIconSize(QSize(50, 50))

        self.horizontalLayout_27.addWidget(self.returnBtn_4)


        self.horizontalLayout_25.addWidget(self.leftSubContainer_5, 0, Qt.AlignLeft)

        self.midSubContainer_5 = QWidget(self.upperContainer_5)
        self.midSubContainer_5.setObjectName(u"midSubContainer_5")
        self.horizontalLayout_28 = QHBoxLayout(self.midSubContainer_5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.superclusterLogo_5 = QLabel(self.midSubContainer_5)
        self.superclusterLogo_5.setObjectName(u"superclusterLogo_5")
        self.superclusterLogo_5.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_5.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_5.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_5.setScaledContents(True)
        self.superclusterLogo_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.superclusterLogo_5)


        self.horizontalLayout_25.addWidget(self.midSubContainer_5, 0, Qt.AlignHCenter)

        self.rightSubContainer_5 = QWidget(self.upperContainer_5)
        self.rightSubContainer_5.setObjectName(u"rightSubContainer_5")
        self.horizontalLayout_29 = QHBoxLayout(self.rightSubContainer_5)
        self.horizontalLayout_29.setSpacing(20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_5 = QPushButton(self.rightSubContainer_5)
        self.settingsBtn_5.setObjectName(u"settingsBtn_5")
        self.settingsBtn_5.setMinimumSize(QSize(0, 50))
        self.settingsBtn_5.setMaximumSize(QSize(50, 50))
        self.settingsBtn_5.setStyleSheet(u"")
        self.settingsBtn_5.setIcon(icon1)
        self.settingsBtn_5.setIconSize(QSize(50, 50))

        self.horizontalLayout_29.addWidget(self.settingsBtn_5)

        self.infoBtn_5 = QPushButton(self.rightSubContainer_5)
        self.infoBtn_5.setObjectName(u"infoBtn_5")
        self.infoBtn_5.setMinimumSize(QSize(50, 50))
        self.infoBtn_5.setMaximumSize(QSize(100, 100))
        self.infoBtn_5.setStyleSheet(u"")
        self.infoBtn_5.setIcon(icon2)
        self.infoBtn_5.setIconSize(QSize(50, 50))

        self.horizontalLayout_29.addWidget(self.infoBtn_5)


        self.horizontalLayout_25.addWidget(self.rightSubContainer_5, 0, Qt.AlignRight)


        self.verticalLayout_49.addWidget(self.upperContainer_5)

        self.archiveDataLabel_3 = QWidget(self.dataChartsPage)
        self.archiveDataLabel_3.setObjectName(u"archiveDataLabel_3")
        sizePolicy1.setHeightForWidth(self.archiveDataLabel_3.sizePolicy().hasHeightForWidth())
        self.archiveDataLabel_3.setSizePolicy(sizePolicy1)
        self.verticalLayout_37 = QVBoxLayout(self.archiveDataLabel_3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.pageTitleWidget_3 = QWidget(self.archiveDataLabel_3)
        self.pageTitleWidget_3.setObjectName(u"pageTitleWidget_3")
        self.horizontalLayout_30 = QHBoxLayout(self.pageTitleWidget_3)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.pageTitleWidget_3)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_38 = QVBoxLayout(self.widget_22)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 10, 0, 0)
        self.missionLabel_3 = QLabel(self.widget_22)
        self.missionLabel_3.setObjectName(u"missionLabel_3")
        self.missionLabel_3.setFont(font)

        self.verticalLayout_38.addWidget(self.missionLabel_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_30.addWidget(self.widget_22)

        self.titleLabel_3 = QWidget(self.pageTitleWidget_3)
        self.titleLabel_3.setObjectName(u"titleLabel_3")
        self.verticalLayout_39 = QVBoxLayout(self.titleLabel_3)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.titleLabel_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_39.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_30.addWidget(self.titleLabel_3)

        self.widget_23 = QWidget(self.pageTitleWidget_3)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_40 = QVBoxLayout(self.widget_23)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 10, 0, 0)
        self.label_11 = QLabel(self.widget_23)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_40.addWidget(self.label_11, 0, Qt.AlignHCenter)


        self.horizontalLayout_30.addWidget(self.widget_23)


        self.verticalLayout_37.addWidget(self.pageTitleWidget_3)

        self.separatorWidget_3 = QWidget(self.archiveDataLabel_3)
        self.separatorWidget_3.setObjectName(u"separatorWidget_3")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.separatorWidget_3.sizePolicy().hasHeightForWidth())
        self.separatorWidget_3.setSizePolicy(sizePolicy10)
        self.verticalLayout_47 = QVBoxLayout(self.separatorWidget_3)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.line_4 = QFrame(self.separatorWidget_3)
        self.line_4.setObjectName(u"line_4")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy11)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_47.addWidget(self.line_4)


        self.verticalLayout_37.addWidget(self.separatorWidget_3)


        self.verticalLayout_49.addWidget(self.archiveDataLabel_3)

        self.mainChartsContainer = QWidget(self.dataChartsPage)
        self.mainChartsContainer.setObjectName(u"mainChartsContainer")
        sizePolicy1.setHeightForWidth(self.mainChartsContainer.sizePolicy().hasHeightForWidth())
        self.mainChartsContainer.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setPointSize(9)
        self.mainChartsContainer.setFont(font9)
        self.mainChartsContainer.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_48 = QVBoxLayout(self.mainChartsContainer)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame = QFrame(self.mainChartsContainer)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setMinimumSize(QSize(50, 180))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_3)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.pressureButton = QPushButton(self.frame_3)
        self.pressureButton.setObjectName(u"pressureButton")
        self.pressureButton.setMinimumSize(QSize(0, 120))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/yellow_pack/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pressureButton.setIcon(icon3)
        self.pressureButton.setIconSize(QSize(100, 100))

        self.verticalLayout_50.addWidget(self.pressureButton)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        font10 = QFont()
        font10.setPointSize(16)
        self.label_12.setFont(font10)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_12)


        self.horizontalLayout_31.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_4)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.outsideTempBtn = QPushButton(self.frame_4)
        self.outsideTempBtn.setObjectName(u"outsideTempBtn")
        self.outsideTempBtn.setMinimumSize(QSize(0, 120))
        self.outsideTempBtn.setIcon(icon3)
        self.outsideTempBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_56.addWidget(self.outsideTempBtn)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font10)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_18)


        self.horizontalLayout_31.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_5)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.tempBmpBtn = QPushButton(self.frame_5)
        self.tempBmpBtn.setObjectName(u"tempBmpBtn")
        self.tempBmpBtn.setMinimumSize(QSize(0, 120))
        self.tempBmpBtn.setIcon(icon3)
        self.tempBmpBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_57.addWidget(self.tempBmpBtn)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.label_19)


        self.horizontalLayout_31.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_6)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.difPressureBtn = QPushButton(self.frame_6)
        self.difPressureBtn.setObjectName(u"difPressureBtn")
        self.difPressureBtn.setMinimumSize(QSize(0, 120))
        self.difPressureBtn.setIcon(icon3)
        self.difPressureBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_58.addWidget(self.difPressureBtn)

        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font10)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_58.addWidget(self.label_20)


        self.horizontalLayout_31.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_7)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.hscTempBtn = QPushButton(self.frame_7)
        self.hscTempBtn.setObjectName(u"hscTempBtn")
        self.hscTempBtn.setMinimumSize(QSize(0, 120))
        self.hscTempBtn.setIcon(icon3)
        self.hscTempBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_59.addWidget(self.hscTempBtn)

        self.label_21 = QLabel(self.frame_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.label_21)


        self.horizontalLayout_31.addWidget(self.frame_7)


        self.verticalLayout_48.addWidget(self.frame)

        self.frame_2 = QFrame(self.mainChartsContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_8)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.windNsBtn = QPushButton(self.frame_8)
        self.windNsBtn.setObjectName(u"windNsBtn")
        self.windNsBtn.setMinimumSize(QSize(0, 120))
        self.windNsBtn.setIcon(icon3)
        self.windNsBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_60.addWidget(self.windNsBtn)

        self.label_22 = QLabel(self.frame_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font10)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_60.addWidget(self.label_22)


        self.horizontalLayout_32.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_9)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.windWeBtn = QPushButton(self.frame_9)
        self.windWeBtn.setObjectName(u"windWeBtn")
        self.windWeBtn.setMinimumSize(QSize(0, 120))
        self.windWeBtn.setIcon(icon3)
        self.windWeBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_61.addWidget(self.windWeBtn)

        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font10)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.label_23)


        self.horizontalLayout_32.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 180))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_10)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.axBtn = QPushButton(self.frame_10)
        self.axBtn.setObjectName(u"axBtn")
        self.axBtn.setMinimumSize(QSize(0, 120))
        self.axBtn.setIcon(icon3)
        self.axBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_62.addWidget(self.axBtn)

        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font10)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_62.addWidget(self.label_24)


        self.horizontalLayout_32.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_11)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.ayBtn = QPushButton(self.frame_11)
        self.ayBtn.setObjectName(u"ayBtn")
        self.ayBtn.setMinimumSize(QSize(0, 120))
        self.ayBtn.setIcon(icon3)
        self.ayBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_63.addWidget(self.ayBtn)

        self.label_26 = QLabel(self.frame_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font10)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_63.addWidget(self.label_26)


        self.horizontalLayout_32.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_12)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.azBtn = QPushButton(self.frame_12)
        self.azBtn.setObjectName(u"azBtn")
        self.azBtn.setMinimumSize(QSize(0, 120))
        self.azBtn.setIcon(icon3)
        self.azBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_64.addWidget(self.azBtn)

        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font10)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_25)


        self.horizontalLayout_32.addWidget(self.frame_12)


        self.verticalLayout_48.addWidget(self.frame_2)


        self.verticalLayout_49.addWidget(self.mainChartsContainer)

        self.widget_4 = QWidget(self.dataChartsPage)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(2)
        sizePolicy12.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy12)
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.voidRtnBtn = QPushButton(self.widget_4)
        self.voidRtnBtn.setObjectName(u"voidRtnBtn")
        self.voidRtnBtn.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/yellow_pack/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.voidRtnBtn.setIcon(icon4)
        self.voidRtnBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_33.addWidget(self.voidRtnBtn)

        self.nxtPgBtn1 = QPushButton(self.widget_4)
        self.nxtPgBtn1.setObjectName(u"nxtPgBtn1")
        self.nxtPgBtn1.setMinimumSize(QSize(0, 30))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/yellow_pack/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nxtPgBtn1.setIcon(icon5)
        self.nxtPgBtn1.setIconSize(QSize(40, 40))

        self.horizontalLayout_33.addWidget(self.nxtPgBtn1)


        self.verticalLayout_49.addWidget(self.widget_4, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.dataChartsPage)
        self.dataChartsPage2 = QWidget()
        self.dataChartsPage2.setObjectName(u"dataChartsPage2")
        self.verticalLayout_81 = QVBoxLayout(self.dataChartsPage2)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.upperContainer_7 = QWidget(self.dataChartsPage2)
        self.upperContainer_7.setObjectName(u"upperContainer_7")
        sizePolicy3.setHeightForWidth(self.upperContainer_7.sizePolicy().hasHeightForWidth())
        self.upperContainer_7.setSizePolicy(sizePolicy3)
        self.upperContainer_7.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_39 = QHBoxLayout(self.upperContainer_7)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_7 = QWidget(self.upperContainer_7)
        self.leftSubContainer_7.setObjectName(u"leftSubContainer_7")
        self.horizontalLayout_40 = QHBoxLayout(self.leftSubContainer_7)
        self.horizontalLayout_40.setSpacing(10)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(20, -1, 20, -1)
        self.returnBtn_6 = QPushButton(self.leftSubContainer_7)
        self.returnBtn_6.setObjectName(u"returnBtn_6")
        self.returnBtn_6.setMaximumSize(QSize(100, 100))
        self.returnBtn_6.setIcon(icon)
        self.returnBtn_6.setIconSize(QSize(50, 50))

        self.horizontalLayout_40.addWidget(self.returnBtn_6)


        self.horizontalLayout_39.addWidget(self.leftSubContainer_7, 0, Qt.AlignLeft)

        self.midSubContainer_7 = QWidget(self.upperContainer_7)
        self.midSubContainer_7.setObjectName(u"midSubContainer_7")
        self.horizontalLayout_41 = QHBoxLayout(self.midSubContainer_7)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.superclusterLogo_7 = QLabel(self.midSubContainer_7)
        self.superclusterLogo_7.setObjectName(u"superclusterLogo_7")
        self.superclusterLogo_7.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_7.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_7.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_7.setScaledContents(True)
        self.superclusterLogo_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.superclusterLogo_7)


        self.horizontalLayout_39.addWidget(self.midSubContainer_7, 0, Qt.AlignHCenter)

        self.rightSubContainer_7 = QWidget(self.upperContainer_7)
        self.rightSubContainer_7.setObjectName(u"rightSubContainer_7")
        self.horizontalLayout_42 = QHBoxLayout(self.rightSubContainer_7)
        self.horizontalLayout_42.setSpacing(20)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_7 = QPushButton(self.rightSubContainer_7)
        self.settingsBtn_7.setObjectName(u"settingsBtn_7")
        self.settingsBtn_7.setMinimumSize(QSize(0, 50))
        self.settingsBtn_7.setMaximumSize(QSize(50, 50))
        self.settingsBtn_7.setStyleSheet(u"")
        self.settingsBtn_7.setIcon(icon1)
        self.settingsBtn_7.setIconSize(QSize(50, 50))

        self.horizontalLayout_42.addWidget(self.settingsBtn_7)

        self.infoBtn_7 = QPushButton(self.rightSubContainer_7)
        self.infoBtn_7.setObjectName(u"infoBtn_7")
        self.infoBtn_7.setMinimumSize(QSize(50, 50))
        self.infoBtn_7.setMaximumSize(QSize(100, 100))
        self.infoBtn_7.setStyleSheet(u"")
        self.infoBtn_7.setIcon(icon2)
        self.infoBtn_7.setIconSize(QSize(50, 50))

        self.horizontalLayout_42.addWidget(self.infoBtn_7)


        self.horizontalLayout_39.addWidget(self.rightSubContainer_7, 0, Qt.AlignRight)


        self.verticalLayout_81.addWidget(self.upperContainer_7)

        self.archiveDataLabel_5 = QWidget(self.dataChartsPage2)
        self.archiveDataLabel_5.setObjectName(u"archiveDataLabel_5")
        sizePolicy1.setHeightForWidth(self.archiveDataLabel_5.sizePolicy().hasHeightForWidth())
        self.archiveDataLabel_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_65 = QVBoxLayout(self.archiveDataLabel_5)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.pageTitleWidget_5 = QWidget(self.archiveDataLabel_5)
        self.pageTitleWidget_5.setObjectName(u"pageTitleWidget_5")
        self.horizontalLayout_43 = QHBoxLayout(self.pageTitleWidget_5)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.pageTitleWidget_5)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_66 = QVBoxLayout(self.widget_31)
        self.verticalLayout_66.setSpacing(0)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 10, 0, 0)
        self.missionLabel_5 = QLabel(self.widget_31)
        self.missionLabel_5.setObjectName(u"missionLabel_5")
        self.missionLabel_5.setFont(font)

        self.verticalLayout_66.addWidget(self.missionLabel_5, 0, Qt.AlignHCenter)


        self.horizontalLayout_43.addWidget(self.widget_31)

        self.titleLabel_5 = QWidget(self.pageTitleWidget_5)
        self.titleLabel_5.setObjectName(u"titleLabel_5")
        self.verticalLayout_67 = QVBoxLayout(self.titleLabel_5)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.titleLabel_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.verticalLayout_67.addWidget(self.label_27, 0, Qt.AlignHCenter)


        self.horizontalLayout_43.addWidget(self.titleLabel_5)

        self.widget_32 = QWidget(self.pageTitleWidget_5)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_68 = QVBoxLayout(self.widget_32)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 10, 0, 0)
        self.label_28 = QLabel(self.widget_32)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.verticalLayout_68.addWidget(self.label_28, 0, Qt.AlignHCenter)


        self.horizontalLayout_43.addWidget(self.widget_32)


        self.verticalLayout_65.addWidget(self.pageTitleWidget_5)

        self.separatorWidget_5 = QWidget(self.archiveDataLabel_5)
        self.separatorWidget_5.setObjectName(u"separatorWidget_5")
        sizePolicy10.setHeightForWidth(self.separatorWidget_5.sizePolicy().hasHeightForWidth())
        self.separatorWidget_5.setSizePolicy(sizePolicy10)
        self.verticalLayout_69 = QVBoxLayout(self.separatorWidget_5)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.line_7 = QFrame(self.separatorWidget_5)
        self.line_7.setObjectName(u"line_7")
        sizePolicy11.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy11)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_69.addWidget(self.line_7)


        self.verticalLayout_65.addWidget(self.separatorWidget_5)


        self.verticalLayout_81.addWidget(self.archiveDataLabel_5)

        self.mainChartsContainer_2 = QWidget(self.dataChartsPage2)
        self.mainChartsContainer_2.setObjectName(u"mainChartsContainer_2")
        sizePolicy1.setHeightForWidth(self.mainChartsContainer_2.sizePolicy().hasHeightForWidth())
        self.mainChartsContainer_2.setSizePolicy(sizePolicy1)
        self.mainChartsContainer_2.setFont(font9)
        self.mainChartsContainer_2.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_70 = QVBoxLayout(self.mainChartsContainer_2)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_13 = QFrame(self.mainChartsContainer_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy4.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy4)
        self.frame_14.setMinimumSize(QSize(50, 180))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_14)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.angPBtn = QPushButton(self.frame_14)
        self.angPBtn.setObjectName(u"angPBtn")
        self.angPBtn.setMinimumSize(QSize(0, 120))
        self.angPBtn.setIcon(icon3)
        self.angPBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_71.addWidget(self.angPBtn)

        self.label_29 = QLabel(self.frame_14)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font10)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_71.addWidget(self.label_29)


        self.horizontalLayout_44.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_15)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.angQBtn = QPushButton(self.frame_15)
        self.angQBtn.setObjectName(u"angQBtn")
        self.angQBtn.setMinimumSize(QSize(0, 120))
        self.angQBtn.setIcon(icon3)
        self.angQBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_72.addWidget(self.angQBtn)

        self.label_30 = QLabel(self.frame_15)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font10)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_72.addWidget(self.label_30)


        self.horizontalLayout_44.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_16)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.angRBtn = QPushButton(self.frame_16)
        self.angRBtn.setObjectName(u"angRBtn")
        self.angRBtn.setMinimumSize(QSize(0, 120))
        self.angRBtn.setIcon(icon3)
        self.angRBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_73.addWidget(self.angRBtn)

        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font10)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_73.addWidget(self.label_31)


        self.horizontalLayout_44.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_17)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.hxBtn = QPushButton(self.frame_17)
        self.hxBtn.setObjectName(u"hxBtn")
        self.hxBtn.setMinimumSize(QSize(0, 120))
        self.hxBtn.setIcon(icon3)
        self.hxBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_74.addWidget(self.hxBtn)

        self.label_32 = QLabel(self.frame_17)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font10)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_74.addWidget(self.label_32)


        self.horizontalLayout_44.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_18)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.hyBtn = QPushButton(self.frame_18)
        self.hyBtn.setObjectName(u"hyBtn")
        self.hyBtn.setMinimumSize(QSize(0, 120))
        self.hyBtn.setIcon(icon3)
        self.hyBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_75.addWidget(self.hyBtn)

        self.label_33 = QLabel(self.frame_18)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font10)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.label_33)


        self.horizontalLayout_44.addWidget(self.frame_18)


        self.verticalLayout_70.addWidget(self.frame_13)

        self.frame_19 = QFrame(self.mainChartsContainer_2)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy4.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy4)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_20)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.hzBtn = QPushButton(self.frame_20)
        self.hzBtn.setObjectName(u"hzBtn")
        self.hzBtn.setMinimumSize(QSize(0, 120))
        self.hzBtn.setIcon(icon3)
        self.hzBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_76.addWidget(self.hzBtn)

        self.label_34 = QLabel(self.frame_20)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font10)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_34)


        self.horizontalLayout_45.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_21)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.radDioBtn = QPushButton(self.frame_21)
        self.radDioBtn.setObjectName(u"radDioBtn")
        self.radDioBtn.setMinimumSize(QSize(0, 120))
        self.radDioBtn.setIcon(icon3)
        self.radDioBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_77.addWidget(self.radDioBtn)

        self.label_35 = QLabel(self.frame_21)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font10)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.label_35)


        self.horizontalLayout_45.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 180))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_22)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.geigBtn = QPushButton(self.frame_22)
        self.geigBtn.setObjectName(u"geigBtn")
        self.geigBtn.setMinimumSize(QSize(0, 120))
        self.geigBtn.setIcon(icon3)
        self.geigBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_78.addWidget(self.geigBtn)

        self.label_36 = QLabel(self.frame_22)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font10)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.label_36)


        self.horizontalLayout_45.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_23)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.iUseBtn = QPushButton(self.frame_23)
        self.iUseBtn.setObjectName(u"iUseBtn")
        self.iUseBtn.setMinimumSize(QSize(0, 120))
        self.iUseBtn.setIcon(icon3)
        self.iUseBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_79.addWidget(self.iUseBtn)

        self.label_37 = QLabel(self.frame_23)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font10)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.label_37)


        self.horizontalLayout_45.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_24)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.batVBtn = QPushButton(self.frame_24)
        self.batVBtn.setObjectName(u"batVBtn")
        self.batVBtn.setMinimumSize(QSize(0, 120))
        self.batVBtn.setIcon(icon3)
        self.batVBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_80.addWidget(self.batVBtn)

        self.label_38 = QLabel(self.frame_24)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font10)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_80.addWidget(self.label_38)


        self.horizontalLayout_45.addWidget(self.frame_24)


        self.verticalLayout_70.addWidget(self.frame_19)


        self.verticalLayout_81.addWidget(self.mainChartsContainer_2)

        self.widget_5 = QWidget(self.dataChartsPage2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy12.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy12)
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_46 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, 0, -1, 0)
        self.rtnBtnPg1 = QPushButton(self.widget_5)
        self.rtnBtnPg1.setObjectName(u"rtnBtnPg1")
        self.rtnBtnPg1.setMinimumSize(QSize(0, 30))
        self.rtnBtnPg1.setIcon(icon4)
        self.rtnBtnPg1.setIconSize(QSize(40, 40))

        self.horizontalLayout_46.addWidget(self.rtnBtnPg1)

        self.fwdBtnPg3 = QPushButton(self.widget_5)
        self.fwdBtnPg3.setObjectName(u"fwdBtnPg3")
        self.fwdBtnPg3.setMinimumSize(QSize(0, 30))
        self.fwdBtnPg3.setIcon(icon5)
        self.fwdBtnPg3.setIconSize(QSize(40, 40))

        self.horizontalLayout_46.addWidget(self.fwdBtnPg3)


        self.verticalLayout_81.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.dataChartsPage2)
        self.dataChartsPage3 = QWidget()
        self.dataChartsPage3.setObjectName(u"dataChartsPage3")
        self.verticalLayout_98 = QVBoxLayout(self.dataChartsPage3)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.upperContainer_8 = QWidget(self.dataChartsPage3)
        self.upperContainer_8.setObjectName(u"upperContainer_8")
        sizePolicy3.setHeightForWidth(self.upperContainer_8.sizePolicy().hasHeightForWidth())
        self.upperContainer_8.setSizePolicy(sizePolicy3)
        self.upperContainer_8.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_47 = QHBoxLayout(self.upperContainer_8)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_8 = QWidget(self.upperContainer_8)
        self.leftSubContainer_8.setObjectName(u"leftSubContainer_8")
        self.horizontalLayout_48 = QHBoxLayout(self.leftSubContainer_8)
        self.horizontalLayout_48.setSpacing(10)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(20, -1, 20, -1)
        self.returnBtn_7 = QPushButton(self.leftSubContainer_8)
        self.returnBtn_7.setObjectName(u"returnBtn_7")
        self.returnBtn_7.setMaximumSize(QSize(100, 100))
        self.returnBtn_7.setIcon(icon)
        self.returnBtn_7.setIconSize(QSize(50, 50))

        self.horizontalLayout_48.addWidget(self.returnBtn_7)


        self.horizontalLayout_47.addWidget(self.leftSubContainer_8, 0, Qt.AlignLeft)

        self.midSubContainer_8 = QWidget(self.upperContainer_8)
        self.midSubContainer_8.setObjectName(u"midSubContainer_8")
        self.horizontalLayout_49 = QHBoxLayout(self.midSubContainer_8)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.superclusterLogo_8 = QLabel(self.midSubContainer_8)
        self.superclusterLogo_8.setObjectName(u"superclusterLogo_8")
        self.superclusterLogo_8.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_8.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_8.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_8.setScaledContents(True)
        self.superclusterLogo_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.superclusterLogo_8)


        self.horizontalLayout_47.addWidget(self.midSubContainer_8, 0, Qt.AlignHCenter)

        self.rightSubContainer_8 = QWidget(self.upperContainer_8)
        self.rightSubContainer_8.setObjectName(u"rightSubContainer_8")
        self.horizontalLayout_50 = QHBoxLayout(self.rightSubContainer_8)
        self.horizontalLayout_50.setSpacing(20)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_8 = QPushButton(self.rightSubContainer_8)
        self.settingsBtn_8.setObjectName(u"settingsBtn_8")
        self.settingsBtn_8.setMinimumSize(QSize(0, 50))
        self.settingsBtn_8.setMaximumSize(QSize(50, 50))
        self.settingsBtn_8.setStyleSheet(u"")
        self.settingsBtn_8.setIcon(icon1)
        self.settingsBtn_8.setIconSize(QSize(50, 50))

        self.horizontalLayout_50.addWidget(self.settingsBtn_8)

        self.infoBtn_8 = QPushButton(self.rightSubContainer_8)
        self.infoBtn_8.setObjectName(u"infoBtn_8")
        self.infoBtn_8.setMinimumSize(QSize(50, 50))
        self.infoBtn_8.setMaximumSize(QSize(100, 100))
        self.infoBtn_8.setStyleSheet(u"")
        self.infoBtn_8.setIcon(icon2)
        self.infoBtn_8.setIconSize(QSize(50, 50))

        self.horizontalLayout_50.addWidget(self.infoBtn_8)


        self.horizontalLayout_47.addWidget(self.rightSubContainer_8, 0, Qt.AlignRight)


        self.verticalLayout_98.addWidget(self.upperContainer_8)

        self.archiveDataLabel_6 = QWidget(self.dataChartsPage3)
        self.archiveDataLabel_6.setObjectName(u"archiveDataLabel_6")
        sizePolicy1.setHeightForWidth(self.archiveDataLabel_6.sizePolicy().hasHeightForWidth())
        self.archiveDataLabel_6.setSizePolicy(sizePolicy1)
        self.verticalLayout_82 = QVBoxLayout(self.archiveDataLabel_6)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.pageTitleWidget_6 = QWidget(self.archiveDataLabel_6)
        self.pageTitleWidget_6.setObjectName(u"pageTitleWidget_6")
        self.horizontalLayout_51 = QHBoxLayout(self.pageTitleWidget_6)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.pageTitleWidget_6)
        self.widget_33.setObjectName(u"widget_33")
        self.verticalLayout_83 = QVBoxLayout(self.widget_33)
        self.verticalLayout_83.setSpacing(0)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.verticalLayout_83.setContentsMargins(0, 10, 0, 0)
        self.missionLabel_6 = QLabel(self.widget_33)
        self.missionLabel_6.setObjectName(u"missionLabel_6")
        self.missionLabel_6.setFont(font)

        self.verticalLayout_83.addWidget(self.missionLabel_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_51.addWidget(self.widget_33)

        self.titleLabel_6 = QWidget(self.pageTitleWidget_6)
        self.titleLabel_6.setObjectName(u"titleLabel_6")
        self.verticalLayout_84 = QVBoxLayout(self.titleLabel_6)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.titleLabel_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.verticalLayout_84.addWidget(self.label_39, 0, Qt.AlignHCenter)


        self.horizontalLayout_51.addWidget(self.titleLabel_6)

        self.widget_34 = QWidget(self.pageTitleWidget_6)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_85 = QVBoxLayout(self.widget_34)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 10, 0, 0)
        self.label_40 = QLabel(self.widget_34)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)

        self.verticalLayout_85.addWidget(self.label_40, 0, Qt.AlignHCenter)


        self.horizontalLayout_51.addWidget(self.widget_34)


        self.verticalLayout_82.addWidget(self.pageTitleWidget_6)

        self.separatorWidget_6 = QWidget(self.archiveDataLabel_6)
        self.separatorWidget_6.setObjectName(u"separatorWidget_6")
        sizePolicy10.setHeightForWidth(self.separatorWidget_6.sizePolicy().hasHeightForWidth())
        self.separatorWidget_6.setSizePolicy(sizePolicy10)
        self.verticalLayout_86 = QVBoxLayout(self.separatorWidget_6)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.line_8 = QFrame(self.separatorWidget_6)
        self.line_8.setObjectName(u"line_8")
        sizePolicy11.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy11)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_86.addWidget(self.line_8)


        self.verticalLayout_82.addWidget(self.separatorWidget_6)


        self.verticalLayout_98.addWidget(self.archiveDataLabel_6)

        self.mainChartsContainer_3 = QWidget(self.dataChartsPage3)
        self.mainChartsContainer_3.setObjectName(u"mainChartsContainer_3")
        sizePolicy1.setHeightForWidth(self.mainChartsContainer_3.sizePolicy().hasHeightForWidth())
        self.mainChartsContainer_3.setSizePolicy(sizePolicy1)
        self.mainChartsContainer_3.setFont(font9)
        self.mainChartsContainer_3.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_87 = QVBoxLayout(self.mainChartsContainer_3)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.frame_25 = QFrame(self.mainChartsContainer_3)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy4.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy4)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy4.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy4)
        self.frame_26.setMinimumSize(QSize(50, 180))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_26)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.gpsSpeedBtn = QPushButton(self.frame_26)
        self.gpsSpeedBtn.setObjectName(u"gpsSpeedBtn")
        self.gpsSpeedBtn.setMinimumSize(QSize(0, 120))
        self.gpsSpeedBtn.setIcon(icon3)
        self.gpsSpeedBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_88.addWidget(self.gpsSpeedBtn)

        self.label_41 = QLabel(self.frame_26)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font10)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.label_41)


        self.horizontalLayout_52.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_27)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.gpsTrackBtn = QPushButton(self.frame_27)
        self.gpsTrackBtn.setObjectName(u"gpsTrackBtn")
        self.gpsTrackBtn.setMinimumSize(QSize(0, 120))
        self.gpsTrackBtn.setIcon(icon3)
        self.gpsTrackBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_89.addWidget(self.gpsTrackBtn)

        self.label_42 = QLabel(self.frame_27)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font10)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_89.addWidget(self.label_42)


        self.horizontalLayout_52.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_28)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.satNumBtn = QPushButton(self.frame_28)
        self.satNumBtn.setObjectName(u"satNumBtn")
        self.satNumBtn.setMinimumSize(QSize(0, 120))
        self.satNumBtn.setIcon(icon3)
        self.satNumBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_90.addWidget(self.satNumBtn)

        self.label_43 = QLabel(self.frame_28)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font10)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_90.addWidget(self.label_43)


        self.horizontalLayout_52.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_29)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.gpsAltBtn = QPushButton(self.frame_29)
        self.gpsAltBtn.setObjectName(u"gpsAltBtn")
        self.gpsAltBtn.setMinimumSize(QSize(0, 120))
        self.gpsAltBtn.setIcon(icon3)
        self.gpsAltBtn.setIconSize(QSize(100, 100))

        self.verticalLayout_91.addWidget(self.gpsAltBtn)

        self.label_44 = QLabel(self.frame_29)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font10)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.verticalLayout_91.addWidget(self.label_44)


        self.horizontalLayout_52.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_25)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_30)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.voidBtn2 = QPushButton(self.frame_30)
        self.voidBtn2.setObjectName(u"voidBtn2")
        self.voidBtn2.setMinimumSize(QSize(0, 120))
        self.voidBtn2.setIcon(icon3)
        self.voidBtn2.setIconSize(QSize(100, 100))

        self.verticalLayout_92.addWidget(self.voidBtn2)

        self.label_45 = QLabel(self.frame_30)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font10)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_92.addWidget(self.label_45)


        self.horizontalLayout_52.addWidget(self.frame_30)


        self.verticalLayout_87.addWidget(self.frame_25)

        self.frame_31 = QFrame(self.mainChartsContainer_3)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy4.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy4)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.frame_32)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.voidBtn3 = QPushButton(self.frame_32)
        self.voidBtn3.setObjectName(u"voidBtn3")
        self.voidBtn3.setMinimumSize(QSize(0, 120))
        self.voidBtn3.setIcon(icon3)
        self.voidBtn3.setIconSize(QSize(100, 100))

        self.verticalLayout_93.addWidget(self.voidBtn3)

        self.label_46 = QLabel(self.frame_32)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font10)
        self.label_46.setAlignment(Qt.AlignCenter)

        self.verticalLayout_93.addWidget(self.label_46)


        self.horizontalLayout_53.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_33)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.voidBtn4 = QPushButton(self.frame_33)
        self.voidBtn4.setObjectName(u"voidBtn4")
        self.voidBtn4.setMinimumSize(QSize(0, 120))
        self.voidBtn4.setIcon(icon3)
        self.voidBtn4.setIconSize(QSize(100, 100))

        self.verticalLayout_94.addWidget(self.voidBtn4)

        self.label_47 = QLabel(self.frame_33)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font10)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.label_47)


        self.horizontalLayout_53.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 180))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_34)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.voidBtn5 = QPushButton(self.frame_34)
        self.voidBtn5.setObjectName(u"voidBtn5")
        self.voidBtn5.setMinimumSize(QSize(0, 120))
        self.voidBtn5.setIcon(icon3)
        self.voidBtn5.setIconSize(QSize(100, 100))

        self.verticalLayout_95.addWidget(self.voidBtn5)

        self.label_48 = QLabel(self.frame_34)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font10)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_95.addWidget(self.label_48)


        self.horizontalLayout_53.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_31)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_35)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.voidBtn6 = QPushButton(self.frame_35)
        self.voidBtn6.setObjectName(u"voidBtn6")
        self.voidBtn6.setMinimumSize(QSize(0, 120))
        self.voidBtn6.setIcon(icon3)
        self.voidBtn6.setIconSize(QSize(100, 100))

        self.verticalLayout_96.addWidget(self.voidBtn6)

        self.label_49 = QLabel(self.frame_35)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font10)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_96.addWidget(self.label_49)


        self.horizontalLayout_53.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_31)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_36)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.voidBtn7 = QPushButton(self.frame_36)
        self.voidBtn7.setObjectName(u"voidBtn7")
        self.voidBtn7.setMinimumSize(QSize(0, 120))
        self.voidBtn7.setIcon(icon3)
        self.voidBtn7.setIconSize(QSize(100, 100))

        self.verticalLayout_97.addWidget(self.voidBtn7)

        self.label_50 = QLabel(self.frame_36)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font10)
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.label_50)


        self.horizontalLayout_53.addWidget(self.frame_36)


        self.verticalLayout_87.addWidget(self.frame_31)


        self.verticalLayout_98.addWidget(self.mainChartsContainer_3)

        self.widget_6 = QWidget(self.dataChartsPage3)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy12.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy12)
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_54 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(-1, 0, -1, 0)
        self.rtnBtnPg2 = QPushButton(self.widget_6)
        self.rtnBtnPg2.setObjectName(u"rtnBtnPg2")
        self.rtnBtnPg2.setMinimumSize(QSize(0, 30))
        self.rtnBtnPg2.setIcon(icon4)
        self.rtnBtnPg2.setIconSize(QSize(40, 40))

        self.horizontalLayout_54.addWidget(self.rtnBtnPg2)

        self.voidBtn8 = QPushButton(self.widget_6)
        self.voidBtn8.setObjectName(u"voidBtn8")
        self.voidBtn8.setMinimumSize(QSize(0, 30))
        self.voidBtn8.setIcon(icon5)
        self.voidBtn8.setIconSize(QSize(40, 40))

        self.horizontalLayout_54.addWidget(self.voidBtn8)


        self.verticalLayout_98.addWidget(self.widget_6)

        self.stackedWidget.addWidget(self.dataChartsPage3)
        self.pressureChartPage = QWidget()
        self.pressureChartPage.setObjectName(u"pressureChartPage")
        self.upperContainer_6 = QWidget(self.pressureChartPage)
        self.upperContainer_6.setObjectName(u"upperContainer_6")
        self.upperContainer_6.setGeometry(QRect(10, 10, 1237, 102))
        sizePolicy3.setHeightForWidth(self.upperContainer_6.sizePolicy().hasHeightForWidth())
        self.upperContainer_6.setSizePolicy(sizePolicy3)
        self.upperContainer_6.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_34 = QHBoxLayout(self.upperContainer_6)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.leftSubContainer_6 = QWidget(self.upperContainer_6)
        self.leftSubContainer_6.setObjectName(u"leftSubContainer_6")
        self.horizontalLayout_35 = QHBoxLayout(self.leftSubContainer_6)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(20, -1, 20, -1)
        self.returnBtn_5 = QPushButton(self.leftSubContainer_6)
        self.returnBtn_5.setObjectName(u"returnBtn_5")
        self.returnBtn_5.setMaximumSize(QSize(100, 100))
        self.returnBtn_5.setIcon(icon)
        self.returnBtn_5.setIconSize(QSize(50, 50))

        self.horizontalLayout_35.addWidget(self.returnBtn_5)


        self.horizontalLayout_34.addWidget(self.leftSubContainer_6, 0, Qt.AlignLeft)

        self.midSubContainer_6 = QWidget(self.upperContainer_6)
        self.midSubContainer_6.setObjectName(u"midSubContainer_6")
        self.horizontalLayout_36 = QHBoxLayout(self.midSubContainer_6)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.superclusterLogo_6 = QLabel(self.midSubContainer_6)
        self.superclusterLogo_6.setObjectName(u"superclusterLogo_6")
        self.superclusterLogo_6.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_6.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_6.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_6.setScaledContents(True)
        self.superclusterLogo_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.superclusterLogo_6)


        self.horizontalLayout_34.addWidget(self.midSubContainer_6, 0, Qt.AlignHCenter)

        self.rightSubContainer_6 = QWidget(self.upperContainer_6)
        self.rightSubContainer_6.setObjectName(u"rightSubContainer_6")
        self.horizontalLayout_37 = QHBoxLayout(self.rightSubContainer_6)
        self.horizontalLayout_37.setSpacing(20)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(20, -1, 20, -1)
        self.settingsBtn_6 = QPushButton(self.rightSubContainer_6)
        self.settingsBtn_6.setObjectName(u"settingsBtn_6")
        self.settingsBtn_6.setMinimumSize(QSize(0, 50))
        self.settingsBtn_6.setMaximumSize(QSize(50, 50))
        self.settingsBtn_6.setStyleSheet(u"")
        self.settingsBtn_6.setIcon(icon1)
        self.settingsBtn_6.setIconSize(QSize(50, 50))

        self.horizontalLayout_37.addWidget(self.settingsBtn_6)

        self.infoBtn_6 = QPushButton(self.rightSubContainer_6)
        self.infoBtn_6.setObjectName(u"infoBtn_6")
        self.infoBtn_6.setMinimumSize(QSize(50, 50))
        self.infoBtn_6.setMaximumSize(QSize(100, 100))
        self.infoBtn_6.setStyleSheet(u"")
        self.infoBtn_6.setIcon(icon2)
        self.infoBtn_6.setIconSize(QSize(50, 50))

        self.horizontalLayout_37.addWidget(self.infoBtn_6)


        self.horizontalLayout_34.addWidget(self.rightSubContainer_6, 0, Qt.AlignRight)

        self.archiveDataLabel_4 = QWidget(self.pressureChartPage)
        self.archiveDataLabel_4.setObjectName(u"archiveDataLabel_4")
        self.archiveDataLabel_4.setGeometry(QRect(10, 120, 1237, 72))
        self.verticalLayout_51 = QVBoxLayout(self.archiveDataLabel_4)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.pageTitleWidget_4 = QWidget(self.archiveDataLabel_4)
        self.pageTitleWidget_4.setObjectName(u"pageTitleWidget_4")
        self.horizontalLayout_38 = QHBoxLayout(self.pageTitleWidget_4)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.pageTitleWidget_4)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_52 = QVBoxLayout(self.widget_24)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 10, 0, 0)
        self.missionLabel_4 = QLabel(self.widget_24)
        self.missionLabel_4.setObjectName(u"missionLabel_4")
        self.missionLabel_4.setFont(font)

        self.verticalLayout_52.addWidget(self.missionLabel_4, 0, Qt.AlignHCenter)


        self.horizontalLayout_38.addWidget(self.widget_24)

        self.titleLabel_4 = QWidget(self.pageTitleWidget_4)
        self.titleLabel_4.setObjectName(u"titleLabel_4")
        self.verticalLayout_53 = QVBoxLayout(self.titleLabel_4)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.titleLabel_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_53.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.horizontalLayout_38.addWidget(self.titleLabel_4)

        self.widget_25 = QWidget(self.pageTitleWidget_4)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_54 = QVBoxLayout(self.widget_25)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 10, 0, 0)
        self.label_17 = QLabel(self.widget_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_54.addWidget(self.label_17, 0, Qt.AlignHCenter)


        self.horizontalLayout_38.addWidget(self.widget_25)


        self.verticalLayout_51.addWidget(self.pageTitleWidget_4)

        self.separatorWidget_4 = QWidget(self.archiveDataLabel_4)
        self.separatorWidget_4.setObjectName(u"separatorWidget_4")
        self.verticalLayout_55 = QVBoxLayout(self.separatorWidget_4)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.separatorWidget_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_55.addWidget(self.line_6)


        self.verticalLayout_51.addWidget(self.separatorWidget_4)

        self.pressurePlot = MplWidget(self.pressureChartPage)
        self.pressurePlot.setObjectName(u"pressurePlot")
        self.pressurePlot.setGeometry(QRect(10, 200, 1241, 491))
        self.stackedWidget.addWidget(self.pressureChartPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.returnBtn.setText("")
        self.superclusterLogo.setText("")
        self.settingsBtn.setText("")
        self.infoBtn.setText("")
        self.missionLabel.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ARCHIVE DATA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select file:", None))
        self.filePathLabel.setText("")
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mission duration:", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.chartsBtn.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
        self.superclusterLogo_2.setText("")
        self.settingsBtn_2.setText("")
        self.infoBtn_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"HOME PAGE", None))
        self.liveDataIcon.setText("")
        self.liveDataBtn.setText(QCoreApplication.translate("MainWindow", u"LIVE DATA", None))
        self.archiveDataIcon.setText("")
        self.archiveDataBtn.setText(QCoreApplication.translate("MainWindow", u"ARCHIVE DATA", None))
        self.returnBtn_2.setText("")
        self.superclusterLogo_3.setText("")
        self.settingsBtn_3.setText("")
        self.infoBtn_3.setText("")
        self.missionLabel_2.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LIVE DATA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.connectBtn.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lora", None))
        self.dataBtn_2.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.chartsBtn_2.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
        self.returnBtn_3.setText("")
        self.superclusterLogo_4.setText("")
        self.settingsBtn_4.setText("")
        self.infoBtn_4.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Mission time [s]", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pressure [hPa]", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Temperature [deg C]", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sattelite number [-]", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Latitude [deg]", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Longitude [deg]", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Speed [km/h]", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Height [m]", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Track [deg]", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Battery voltage [V]", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Current Use [A]", None));
        self.returnBtn_4.setText("")
        self.superclusterLogo_5.setText("")
        self.settingsBtn_5.setText("")
        self.infoBtn_5.setText("")
        self.missionLabel_3.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DATA CHARTS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        self.pressureButton.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.outsideTempBtn.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Outside Air Temp", None))
        self.tempBmpBtn.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Temp BMP", None))
        self.difPressureBtn.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Dif Pressure", None))
        self.hscTempBtn.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"HSC Temp", None))
        self.windNsBtn.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Wind NS", None))
        self.windWeBtn.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Wind WE", None))
        self.axBtn.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"A_x", None))
        self.ayBtn.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"A_y", None))
        self.azBtn.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"A_z", None))
        self.voidRtnBtn.setText("")
        self.nxtPgBtn1.setText("")
        self.returnBtn_6.setText("")
        self.superclusterLogo_7.setText("")
        self.settingsBtn_7.setText("")
        self.infoBtn_7.setText("")
        self.missionLabel_5.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"DATA CHARTS", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        self.angPBtn.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Ang_p", None))
        self.angQBtn.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Ang_q", None))
        self.angRBtn.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Ang_r", None))
        self.hxBtn.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Hx", None))
        self.hyBtn.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Hy", None))
        self.hzBtn.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.radDioBtn.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Diode Radiation", None))
        self.geigBtn.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Geiger Radiation", None))
        self.iUseBtn.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Currant Use", None))
        self.batVBtn.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Battery Voltage", None))
        self.rtnBtnPg1.setText("")
        self.fwdBtnPg3.setText("")
        self.returnBtn_7.setText("")
        self.superclusterLogo_8.setText("")
        self.settingsBtn_8.setText("")
        self.infoBtn_8.setText("")
        self.missionLabel_6.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"DATA CHARTS", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        self.gpsSpeedBtn.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"GPS Speed", None))
        self.gpsTrackBtn.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"GPS Track", None))
        self.satNumBtn.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Sattelite Number", None))
        self.gpsAltBtn.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"GPS Altitude", None))
        self.voidBtn2.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.voidBtn3.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.voidBtn4.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.voidBtn5.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.voidBtn6.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.voidBtn7.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.rtnBtnPg2.setText("")
        self.voidBtn8.setText("")
        self.returnBtn_5.setText("")
        self.superclusterLogo_6.setText("")
        self.settingsBtn_6.setText("")
        self.infoBtn_6.setText("")
        self.missionLabel_4.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CHART", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
    # retranslateUi

