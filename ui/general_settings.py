# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general-settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 493)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
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
        self.label_4.setStyleSheet("font: 18pt \"MS UI Gothic\";\n"
"color: rgb(170, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
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
        self.pushButton_3.setText(_translate("MainWindow", "RESTORE BACKUP"))
        self.pushButton.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.pushButton_2.setText(_translate("MainWindow", "<  BACK TO PREVIOUS MENU"))
