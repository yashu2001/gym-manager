# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general-settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 355)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 18pt \"MS UI Gothic\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("2.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 18pt \"MS UI Gothic\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">GENERAL SETTINGS</p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.pushButton_2.setText(_translate("MainWindow", "BACK TO PREVIOUS MENU"))
