# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archiveDataDATA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

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
        self.stackedWidget.setGeometry(QRect(-10, 0, 1291, 741))
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
        self.verticalLayout_2 = QVBoxLayout(self.mainContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.mainContainer)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
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
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        font2 = QFont()
        font2.setFamily(u"Inria Sans")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.tableWidget.setFont(font2)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(119)

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.mainContainer)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.returnBtn.setText("")
        self.superclusterLogo.setText("")
        self.settingsBtn.setText("")
        self.infoBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mission ID: <nr>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Launch Data: <data>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"time", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"pressure", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"temperature", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"9", None));
    # retranslateUi

