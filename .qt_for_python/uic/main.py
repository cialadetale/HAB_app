# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 738)
        MainWindow.setStyleSheet(u"*{\n"
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
"#settingsBtn, #infoBtn, #liveDataIcon, #archiveDataIcon{\n"
" border: none;\n"
" background-color: transparent;\n"
"}\n"
"\n"
"#liveDataBtn:hover, #archiveDataBtn:hover{\n"
" border: none;\n"
" background-color: rgb(242, 157, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.upperContainer = QWidget(self.centralwidget)
        self.upperContainer.setObjectName(u"upperContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperContainer.sizePolicy().hasHeightForWidth())
        self.upperContainer.setSizePolicy(sizePolicy)
        self.upperContainer.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_2 = QHBoxLayout(self.upperContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 50)
        self.infoBtn = QPushButton(self.upperContainer)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(50, 50))
        self.infoBtn.setMaximumSize(QSize(16777215, 50))
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
        icon = QIcon()
        icon.addFile(u":/icons/icons/yellow_pack/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon)
        self.infoBtn.setIconSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.infoBtn, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_2 = QLabel(self.upperContainer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(110, 80))
        self.label_2.setMaximumSize(QSize(110, 80))
        self.label_2.setPixmap(QPixmap(u":/pixmap/icons/logo/logo_3.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.settingsBtn = QPushButton(self.upperContainer)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(50, 50))
        self.settingsBtn.setMaximumSize(QSize(16777215, 50))
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

        self.horizontalLayout_2.addWidget(self.settingsBtn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.upperContainer)

        self.welcomeWidget = QWidget(self.centralwidget)
        self.welcomeWidget.setObjectName(u"welcomeWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.welcomeWidget.sizePolicy().hasHeightForWidth())
        self.welcomeWidget.setSizePolicy(sizePolicy1)
        self.welcomeWidget.setMinimumSize(QSize(0, 100))
        self.welcomeWidget.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_4 = QVBoxLayout(self.welcomeWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(200, -1, 200, 20)
        self.welcomeLabel = QLabel(self.welcomeWidget)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        font = QFont()
        font.setFamily(u"Inria Sans")
        font.setPointSize(28)
        self.welcomeLabel.setFont(font)

        self.verticalLayout_4.addWidget(self.welcomeLabel, 0, Qt.AlignHCenter)

        self.horizontalLine = QFrame(self.welcomeWidget)
        self.horizontalLine.setObjectName(u"horizontalLine")
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.horizontalLine)


        self.verticalLayout.addWidget(self.welcomeWidget, 0, Qt.AlignBottom)

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.mainContainer)
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 50, 50, 50)
        self.liveDataContainer = QWidget(self.mainContainer)
        self.liveDataContainer.setObjectName(u"liveDataContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.liveDataContainer.sizePolicy().hasHeightForWidth())
        self.liveDataContainer.setSizePolicy(sizePolicy3)
        self.liveDataContainer.setMaximumSize(QSize(900, 600))
        self.verticalLayout_3 = QVBoxLayout(self.liveDataContainer)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.liveDataIcon = QLabel(self.liveDataContainer)
        self.liveDataIcon.setObjectName(u"liveDataIcon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.liveDataIcon.sizePolicy().hasHeightForWidth())
        self.liveDataIcon.setSizePolicy(sizePolicy4)
        self.liveDataIcon.setMaximumSize(QSize(16777215, 16777215))
        self.liveDataIcon.setPixmap(QPixmap(u":/pixmap/icons/pin.png"))
        self.liveDataIcon.setScaledContents(False)
        self.liveDataIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.liveDataIcon, 0, Qt.AlignHCenter)

        self.liveDataBtn = QPushButton(self.liveDataContainer)
        self.liveDataBtn.setObjectName(u"liveDataBtn")
        self.liveDataBtn.setMinimumSize(QSize(300, 80))
        font1 = QFont()
        font1.setFamily(u"Inria Sans")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)
        self.liveDataBtn.setFont(font1)

        self.verticalLayout_3.addWidget(self.liveDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.liveDataContainer)

        self.archiveDataContainer = QWidget(self.mainContainer)
        self.archiveDataContainer.setObjectName(u"archiveDataContainer")
        sizePolicy3.setHeightForWidth(self.archiveDataContainer.sizePolicy().hasHeightForWidth())
        self.archiveDataContainer.setSizePolicy(sizePolicy3)
        self.archiveDataContainer.setMaximumSize(QSize(900, 600))
        self.verticalLayout_2 = QVBoxLayout(self.archiveDataContainer)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.archiveDataIcon = QLabel(self.archiveDataContainer)
        self.archiveDataIcon.setObjectName(u"archiveDataIcon")
        sizePolicy4.setHeightForWidth(self.archiveDataIcon.sizePolicy().hasHeightForWidth())
        self.archiveDataIcon.setSizePolicy(sizePolicy4)
        self.archiveDataIcon.setMaximumSize(QSize(16777215, 16777215))
        self.archiveDataIcon.setPixmap(QPixmap(u":/pixmap/icons/plot.png"))
        self.archiveDataIcon.setScaledContents(False)
        self.archiveDataIcon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.archiveDataIcon, 0, Qt.AlignHCenter)

        self.archiveDataBtn = QPushButton(self.archiveDataContainer)
        self.archiveDataBtn.setObjectName(u"archiveDataBtn")
        sizePolicy4.setHeightForWidth(self.archiveDataBtn.sizePolicy().hasHeightForWidth())
        self.archiveDataBtn.setSizePolicy(sizePolicy4)
        self.archiveDataBtn.setMinimumSize(QSize(300, 80))
        font2 = QFont()
        font2.setFamily(u"Inria Sans")
        font2.setPointSize(18)
        self.archiveDataBtn.setFont(font2)

        self.verticalLayout_2.addWidget(self.archiveDataBtn, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.archiveDataContainer)


        self.verticalLayout.addWidget(self.mainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.infoBtn.setText("")
        self.label_2.setText("")
        self.settingsBtn.setText("")
        self.welcomeLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.liveDataIcon.setText("")
        self.liveDataBtn.setText(QCoreApplication.translate("MainWindow", u"LIVE DATA", None))
        self.archiveDataIcon.setText("")
        self.archiveDataBtn.setText(QCoreApplication.translate("MainWindow", u"ARCHIVE DATA", None))
    # retranslateUi

