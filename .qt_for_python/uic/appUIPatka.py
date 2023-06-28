# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appUIPatka.ui'
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
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
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
"#settingsBtn, #infoBtn, #liveDataIcon, #archiveDataIcon, #returnBtn, #settingsBtn_2, #infoBtn_2, #settingsBtn_3, #infoBtn_3, #returnBtn_2, #settingsBtn_4, #infoBtn_4, #returnBtn_3{\n"
" border: none;\n"
" background-color: transparent;\n"
"}\n"
"\n"
"#liveDataBtn:hover, #archiveDataBtn:hover{\n"
" border: none;\n"
" background-color: rgb(242, 157, 0);\n"
"}\n"
"\n"
"#addFile, #buttons, #missionDuration, #mapContainer, #bluetoothWidget,  #loraWidget,#buttons_2, #missionDuration_2 {\n"
" background-color: #F4F4F4;\n"
" border-radius: 20px;\n"
"}\n"
"\n"
"#widget_2, #widget_7, #widget_8, #widget_9, #widget_13, #label_4, #label_5, #widget_3, #label_10, #widget_17, #label_9, #widget_19,#widget_20,#widget_21, #widget_31, #widget_32, #label_16, #label_17{\n"
" "
                        "background-color: #F4F4F4;\n"
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
"")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 1281, 731))
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.archiveData = QWidget()
        self.archiveData.setObjectName(u"archiveData")
        sizePolicy.setHeightForWidth(self.archiveData.sizePolicy().hasHeightForWidth())
        self.archiveData.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.archiveData)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.upperContainer = QWidget(self.archiveData)
        self.upperContainer.setObjectName(u"upperContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.upperContainer.sizePolicy().hasHeightForWidth())
        self.upperContainer.setSizePolicy(sizePolicy2)
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


        self.verticalLayout.addWidget(self.upperContainer, 0, Qt.AlignTop)

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


        self.verticalLayout.addWidget(self.archiveDataLabel, 0, Qt.AlignTop)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mapWidget.sizePolicy().hasHeightForWidth())
        self.mapWidget.setSizePolicy(sizePolicy3)

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
        self.filePathLabel = QPlainTextEdit(self.widget_9)
        self.filePathLabel.setObjectName(u"filePathLabel")
        self.filePathLabel.setMinimumSize(QSize(0, 0))
        self.filePathLabel.setMaximumSize(QSize(600, 30))

        self.verticalLayout_11.addWidget(self.filePathLabel)


        self.verticalLayout_6.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.addFile)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.uploadBtn = QPushButton(self.widget_8)
        self.uploadBtn.setObjectName(u"uploadBtn")
        self.uploadBtn.setMinimumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamily(u"Inria Sans")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.uploadBtn.setFont(font3)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dataBtn.sizePolicy().hasHeightForWidth())
        self.dataBtn.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamily(u"Inria Sans")
        font4.setPointSize(16)
        font4.setBold(False)
        font4.setWeight(50)
        self.dataBtn.setFont(font4)

        self.horizontalLayout_4.addWidget(self.dataBtn)

        self.chartsBtn = QPushButton(self.buttons)
        self.chartsBtn.setObjectName(u"chartsBtn")
        sizePolicy4.setHeightForWidth(self.chartsBtn.sizePolicy().hasHeightForWidth())
        self.chartsBtn.setSizePolicy(sizePolicy4)
        self.chartsBtn.setFont(font4)

        self.horizontalLayout_4.addWidget(self.chartsBtn)


        self.verticalLayout_3.addWidget(self.buttons)


        self.horizontalLayout_3.addWidget(self.fileContainer)


        self.verticalLayout.addWidget(self.mainContainer)

        self.stackedWidget.addWidget(self.archiveData)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.verticalLayout_47 = QVBoxLayout(self.page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.upperContainer_4 = QWidget(self.page)
        self.upperContainer_4.setObjectName(u"upperContainer_4")
        sizePolicy2.setHeightForWidth(self.upperContainer_4.sizePolicy().hasHeightForWidth())
        self.upperContainer_4.setSizePolicy(sizePolicy2)
        self.upperContainer_4.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_21 = QHBoxLayout(self.upperContainer_4)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.upperContainer_4)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_22 = QHBoxLayout(self.widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.returnBtn_3 = QPushButton(self.widget)
        self.returnBtn_3.setObjectName(u"returnBtn_3")
        self.returnBtn_3.setMaximumSize(QSize(50, 50))
        self.returnBtn_3.setIcon(icon)
        self.returnBtn_3.setIconSize(QSize(50, 50))

        self.horizontalLayout_22.addWidget(self.returnBtn_3)


        self.horizontalLayout_21.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_4 = QWidget(self.upperContainer_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.superclusterLogo_4 = QLabel(self.widget_4)
        self.superclusterLogo_4.setObjectName(u"superclusterLogo_4")
        self.superclusterLogo_4.setMinimumSize(QSize(110, 80))
        self.superclusterLogo_4.setMaximumSize(QSize(110, 80))
        self.superclusterLogo_4.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.superclusterLogo_4.setScaledContents(True)
        self.superclusterLogo_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.superclusterLogo_4)


        self.horizontalLayout_21.addWidget(self.widget_4, 0, Qt.AlignHCenter)

        self.widget_5 = QWidget(self.upperContainer_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.settingsBtn_4 = QPushButton(self.widget_5)
        self.settingsBtn_4.setObjectName(u"settingsBtn_4")
        self.settingsBtn_4.setMinimumSize(QSize(0, 50))
        self.settingsBtn_4.setMaximumSize(QSize(50, 50))
        self.settingsBtn_4.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/hover_icons/icons/hover/settings.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-repeat: no-repeat;\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
"")
        self.settingsBtn_4.setIcon(icon1)
        self.settingsBtn_4.setIconSize(QSize(50, 50))

        self.horizontalLayout_24.addWidget(self.settingsBtn_4)

        self.infoBtn_4 = QPushButton(self.widget_5)
        self.infoBtn_4.setObjectName(u"infoBtn_4")
        self.infoBtn_4.setMinimumSize(QSize(50, 50))
        self.infoBtn_4.setMaximumSize(QSize(50, 50))
        self.infoBtn_4.setStyleSheet(u"\n"
"\n"
"QPushButton:hover {\n"
"    border-image: url(:/hover_icons/icons/hover/info.svg);\n"
"    background-repeat: no-repeat;\n"
"    background-repeat: no-repeat;\n"
"    width: 50px;\n"
"    height: 50px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/hover_icons/icons/hover/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn_4.setIcon(icon3)
        self.infoBtn_4.setIconSize(QSize(50, 50))

        self.horizontalLayout_24.addWidget(self.infoBtn_4)


        self.horizontalLayout_21.addWidget(self.widget_5, 0, Qt.AlignRight)


        self.verticalLayout_47.addWidget(self.upperContainer_4)

        self.archiveDataLabel_2 = QWidget(self.page)
        self.archiveDataLabel_2.setObjectName(u"archiveDataLabel_2")
        self.verticalLayout_41 = QVBoxLayout(self.archiveDataLabel_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.widget_26 = QWidget(self.archiveDataLabel_2)
        self.widget_26.setObjectName(u"widget_26")
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


        self.verticalLayout_47.addWidget(self.archiveDataLabel_2)

        self.mainContainer_3 = QWidget(self.page)
        self.mainContainer_3.setObjectName(u"mainContainer_3")
        sizePolicy.setHeightForWidth(self.mainContainer_3.sizePolicy().hasHeightForWidth())
        self.mainContainer_3.setSizePolicy(sizePolicy)
        self.verticalLayout_46 = QVBoxLayout(self.mainContainer_3)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.tableWidget_2 = QTableWidget(self.mainContainer_3)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tableWidget_2.rowCount() < 20):
            self.tableWidget_2.setRowCount(20)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem23)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setFont(font2)
        self.tableWidget_2.setRowCount(20)
        self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(119)

        self.verticalLayout_46.addWidget(self.tableWidget_2)


        self.verticalLayout_47.addWidget(self.mainContainer_3)

        self.stackedWidget.addWidget(self.page)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        sizePolicy.setHeightForWidth(self.mainPage.sizePolicy().hasHeightForWidth())
        self.mainPage.setSizePolicy(sizePolicy)
        self.verticalLayout_18 = QVBoxLayout(self.mainPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.upperContainer_2 = QWidget(self.mainPage)
        self.upperContainer_2.setObjectName(u"upperContainer_2")
        sizePolicy2.setHeightForWidth(self.upperContainer_2.sizePolicy().hasHeightForWidth())
        self.upperContainer_2.setSizePolicy(sizePolicy2)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.liveDataContainer.sizePolicy().hasHeightForWidth())
        self.liveDataContainer.setSizePolicy(sizePolicy5)
        self.liveDataContainer.setMaximumSize(QSize(900, 600))
        self.verticalLayout_16 = QVBoxLayout(self.liveDataContainer)
        self.verticalLayout_16.setSpacing(20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(30, 30, 30, 30)
        self.liveDataIcon = QLabel(self.liveDataContainer)
        self.liveDataIcon.setObjectName(u"liveDataIcon")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.liveDataIcon.sizePolicy().hasHeightForWidth())
        self.liveDataIcon.setSizePolicy(sizePolicy6)
        self.liveDataIcon.setMaximumSize(QSize(16777215, 16777215))
        self.liveDataIcon.setPixmap(QPixmap(u":/pixmap/icons/pin.png"))
        self.liveDataIcon.setScaledContents(False)
        self.liveDataIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.liveDataIcon, 0, Qt.AlignHCenter)

        self.liveDataBtn = QPushButton(self.liveDataContainer)
        self.liveDataBtn.setObjectName(u"liveDataBtn")
        self.liveDataBtn.setMinimumSize(QSize(300, 80))
        font5 = QFont()
        font5.setFamily(u"Inria Sans")
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setWeight(50)
        self.liveDataBtn.setFont(font5)

        self.verticalLayout_16.addWidget(self.liveDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.liveDataContainer)

        self.archiveDataContainer = QWidget(self.homeMainContainer)
        self.archiveDataContainer.setObjectName(u"archiveDataContainer")
        sizePolicy5.setHeightForWidth(self.archiveDataContainer.sizePolicy().hasHeightForWidth())
        self.archiveDataContainer.setSizePolicy(sizePolicy5)
        self.archiveDataContainer.setMaximumSize(QSize(900, 600))
        self.verticalLayout_17 = QVBoxLayout(self.archiveDataContainer)
        self.verticalLayout_17.setSpacing(20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(30, 30, 30, 30)
        self.archiveDataIcon = QLabel(self.archiveDataContainer)
        self.archiveDataIcon.setObjectName(u"archiveDataIcon")
        sizePolicy6.setHeightForWidth(self.archiveDataIcon.sizePolicy().hasHeightForWidth())
        self.archiveDataIcon.setSizePolicy(sizePolicy6)
        self.archiveDataIcon.setMaximumSize(QSize(16777215, 16777215))
        self.archiveDataIcon.setPixmap(QPixmap(u":/pixmap/icons/plot.png"))
        self.archiveDataIcon.setScaledContents(False)
        self.archiveDataIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.archiveDataIcon, 0, Qt.AlignHCenter)

        self.archiveDataBtn = QPushButton(self.archiveDataContainer)
        self.archiveDataBtn.setObjectName(u"archiveDataBtn")
        sizePolicy6.setHeightForWidth(self.archiveDataBtn.sizePolicy().hasHeightForWidth())
        self.archiveDataBtn.setSizePolicy(sizePolicy6)
        self.archiveDataBtn.setMinimumSize(QSize(300, 80))
        font6 = QFont()
        font6.setFamily(u"Inria Sans")
        font6.setPointSize(18)
        self.archiveDataBtn.setFont(font6)

        self.verticalLayout_17.addWidget(self.archiveDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout_8.addWidget(self.archiveDataContainer)


        self.verticalLayout_18.addWidget(self.homeMainContainer, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.mainPage)
        self.liveData = QWidget()
        self.liveData.setObjectName(u"liveData")
        sizePolicy.setHeightForWidth(self.liveData.sizePolicy().hasHeightForWidth())
        self.liveData.setSizePolicy(sizePolicy)
        self.verticalLayout_36 = QVBoxLayout(self.liveData)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.upperContainer_3 = QWidget(self.liveData)
        self.upperContainer_3.setObjectName(u"upperContainer_3")
        sizePolicy2.setHeightForWidth(self.upperContainer_3.sizePolicy().hasHeightForWidth())
        self.upperContainer_3.setSizePolicy(sizePolicy2)
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
        self.verticalLayout_29.setContentsMargins(-1, 5, -1, 5)
        self.widget_17 = QWidget(self.bluetoothWidget)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.widget_17)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 5, -1, 0)
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
        self.verticalLayout_31.setContentsMargins(-1, 0, -1, 0)
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
        self.verticalLayout_32.setContentsMargins(-1, 0, -1, 5)
        self.connectBtn = QPushButton(self.widget_20)
        self.connectBtn.setObjectName(u"connectBtn")
        self.connectBtn.setMinimumSize(QSize(100, 30))
        self.connectBtn.setFont(font3)

        self.verticalLayout_32.addWidget(self.connectBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_29.addWidget(self.widget_20)


        self.verticalLayout_28.addWidget(self.bluetoothWidget, 0, Qt.AlignTop)

        self.loraWidget = QWidget(self.connectionContainer)
        self.loraWidget.setObjectName(u"loraWidget")
        self.verticalLayout_33 = QVBoxLayout(self.loraWidget)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 5, -1, 0)
        self.widget_3 = QWidget(self.loraWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_34 = QVBoxLayout(self.widget_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, 5, -1, 0)
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_34.addWidget(self.label_10)


        self.verticalLayout_33.addWidget(self.widget_3)

        self.widget_21 = QWidget(self.loraWidget)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_35 = QVBoxLayout(self.widget_21)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 0, -1, 0)
        self.missionParamLabel_2 = QPlainTextEdit(self.widget_21)
        self.missionParamLabel_2.setObjectName(u"missionParamLabel_2")
        self.missionParamLabel_2.setMinimumSize(QSize(0, 0))
        self.missionParamLabel_2.setMaximumSize(QSize(600, 30))

        self.verticalLayout_35.addWidget(self.missionParamLabel_2)


        self.verticalLayout_33.addWidget(self.widget_21)


        self.verticalLayout_28.addWidget(self.loraWidget)

        self.missionDuration_2 = QWidget(self.connectionContainer)
        self.missionDuration_2.setObjectName(u"missionDuration_2")
        self.verticalLayout_48 = QVBoxLayout(self.missionDuration_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(-1, 10, -1, 10)
        self.widget_31 = QWidget(self.missionDuration_2)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_49 = QVBoxLayout(self.widget_31)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, 0, -1, 0)
        self.label_16 = QLabel(self.widget_31)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_49.addWidget(self.label_16)

        self.plainTextEdit_3 = QPlainTextEdit(self.widget_31)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_3.setMaximumSize(QSize(600, 30))

        self.verticalLayout_49.addWidget(self.plainTextEdit_3)


        self.verticalLayout_48.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.missionDuration_2)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_50 = QVBoxLayout(self.widget_32)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(-1, 0, -1, 0)
        self.label_17 = QLabel(self.widget_32)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.verticalLayout_50.addWidget(self.label_17)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget_32)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_2.setMaximumSize(QSize(600, 30))

        self.verticalLayout_50.addWidget(self.plainTextEdit_2)


        self.verticalLayout_48.addWidget(self.widget_32)


        self.verticalLayout_28.addWidget(self.missionDuration_2)

        self.buttons_2 = QWidget(self.connectionContainer)
        self.buttons_2.setObjectName(u"buttons_2")
        self.horizontalLayout_20 = QHBoxLayout(self.buttons_2)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, 20, 20, 20)
        self.dataBtn_2 = QPushButton(self.buttons_2)
        self.dataBtn_2.setObjectName(u"dataBtn_2")
        sizePolicy4.setHeightForWidth(self.dataBtn_2.sizePolicy().hasHeightForWidth())
        self.dataBtn_2.setSizePolicy(sizePolicy4)
        self.dataBtn_2.setFont(font4)

        self.horizontalLayout_20.addWidget(self.dataBtn_2)

        self.chartsBtn_2 = QPushButton(self.buttons_2)
        self.chartsBtn_2.setObjectName(u"chartsBtn_2")
        sizePolicy4.setHeightForWidth(self.chartsBtn_2.sizePolicy().hasHeightForWidth())
        self.chartsBtn_2.setSizePolicy(sizePolicy4)
        self.chartsBtn_2.setFont(font4)

        self.horizontalLayout_20.addWidget(self.chartsBtn_2)


        self.verticalLayout_28.addWidget(self.buttons_2)


        self.horizontalLayout_19.addWidget(self.connectionContainer)


        self.verticalLayout_36.addWidget(self.mainContainer_2)

        self.stackedWidget.addWidget(self.liveData)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


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
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mission duration:", None))
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.chartsBtn.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
        self.returnBtn_3.setText("")
        self.superclusterLogo_4.setText("")
        self.settingsBtn_4.setText("")
        self.infoBtn_4.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"pressure", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"temperature", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"9", None));
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
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Mission duration:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Position:", None))
        self.dataBtn_2.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.chartsBtn_2.setText(QCoreApplication.translate("MainWindow", u"CHARTS", None))
    # retranslateUi

