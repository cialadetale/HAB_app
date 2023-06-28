# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archiveData.ui'
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
"#settingsBtn, #infoBtn, #liveDataIcon, #archiveDataIcon{\n"
" border: none;\n"
" background-color: transparent;\n"
"}\n"
"\n"
"#liveDataBtn:hover, #archiveDataBtn:hover{\n"
" border: none;\n"
" background-color: rgb(242, 157, 0);\n"
"}")
        self.upperContainer = QWidget(self.centralwidget)
        self.upperContainer.setObjectName(u"upperContainer")
        self.upperContainer.setGeometry(QRect(0, 0, 1280, 160))
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
        self.infoBtn.setMinimumSize(QSize(0, 50))
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
        self.settingsBtn.setMinimumSize(QSize(0, 50))
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

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setGeometry(QRect(10, 156, 1280, 561))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_3.setSpacing(100)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(50, 50, 50, 50)
        self.mapWidget = mapWidget(self.mainContainer)
        self.mapWidget.setObjectName(u"mapWidget")
        self.mapWidget.setMinimumSize(QSize(600, 0))

        self.horizontalLayout_3.addWidget(self.mapWidget, 0, Qt.AlignLeft)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.infoBtn.setText("")
        self.label_2.setText("")
        self.settingsBtn.setText("")
    # retranslateUi

